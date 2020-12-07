from exceptions import SessionDoesNotExistError
import redis
import secrets
import logging
import json


TOKEN_LIFE_SECS = (60 * 60 * 24)

TOKEN_BYTES = 32

class SessionState:
    def __init__(self, user_id: int, username: str):
        """Create a new SessionState

        Args:
            user_id (int): user's ID
            username (str): user's username
        """
        self.user_id = user_id
        self.username = username

    @classmethod
    def from_json(cls, json_str: str):
        """Load a SessionState from a json string

        Args:
            json_str (str): json SessionState

        Returns:
            SessionState: loaded SessionState
        """
        kv = json.loads(json_str)
        return cls(kv["userId"], kv["username"])
    
    def to_json(self):
        """Return a json string representation

        Returns:
            str: json string SessionState
        """
        kv = dict()
        kv["userId"] = self.user_id
        kv["username"] = self.username
        return json.dumps(kv)

class SessionStore:

    def __init__(self, host, port, max_conn):
        """Create a new SessionStore

        Args:
            host (str): Redis Host
            port (str): Redis Port
            max_conn (int): Max pool connections
        """
        logging.info(f'Trying to connect to redis: @{host}:{port} ({max_conn=})')
        self.pool = redis.ConnectionPool(
            host=host, port=port, max_connections=max_conn, decode_responses=True)
        test = redis.Redis(connection_pool=self.pool)
        test.ping()
        logging.info(f'Connection Succeeded!')

    def create_session(self, user_id, username):
        """Create a new session for a given user_id + username

        Args:
            user_id (int): User's ID
            username (str): User's username

        Returns:
            str: Session token
        """
        token = self._gen_token()
        state = SessionState(user_id, username)
        conn = redis.Redis(connection_pool=self.pool)
        conn.set(token, state.to_json(), ex=TOKEN_LIFE_SECS)
        return token

    def end_session(self, token):
        """Ends a session

        Args:
            token (str): Session token

        Raises:
            SessionDoesNotExistError: token is invalid/session doesn't exist
        """
        conn = redis.Redis(connection_pool=self.pool)
        if conn.get(token) is None:
            raise SessionDoesNotExistError()
        conn.delete(token)

    def get_state(self, token):
        """Return a SessionState

        Args:
            token (str): Session token

        Raises:
            SessionDoesNotExistError: token is invalid/session doesn't exist

        Returns:
            SessionState: User's SessionState
        """
        conn = redis.Redis(connection_pool=self.pool)

        state_str = conn.get(token)
        if state_str is None:
            raise SessionDoesNotExistError()
        state = SessionState.from_json(state_str)

        conn.expire(token, TOKEN_LIFE_SECS)
        return state

    def _gen_token(self):
        """Generates an Authorization token for a session

        Returns:
            str: Random token
        """
        return secrets.token_urlsafe(TOKEN_BYTES)