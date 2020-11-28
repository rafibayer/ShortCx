from exceptions import SessionDoesNotExistError
import redis
import secrets
import logging

# 1 day
TOKEN_LIFE_SECS = (60 * 60 * 24)

TOKEN_BYTES = 32


class SessionStore:

    def __init__(self, host, port, max_conn):
        logging.info(f'Trying to connect to redis: @{host}:{port} ({max_conn=})')
        self.pool = redis.ConnectionPool(
            host=host, port=port, max_connections=max_conn, decode_responses=True)
        test = redis.Redis(connection_pool=self.pool)
        test.ping()
        logging.info(f'Connection Succeeded!')

    def create_session(self, email):
        token = self._gen_token()
        conn = redis.Redis(connection_pool=self.pool)
        conn.set(token, email, ex=TOKEN_LIFE_SECS)
        return token

    def end_session(self, token):
        conn = redis.Redis(connection_pool=self.pool)
        if conn.get(token) is None:
            raise SessionDoesNotExistError()
        conn.delete(token)

    def get_state(self, token):
        conn = redis.Redis(connection_pool=self.pool)
        state = conn.get(token)
        if token is None:
            raise SessionDoesNotExistError()
        conn.expire(token, TOKEN_LIFE_SECS)
        return state

    def _gen_token(self):
        """Generates an Authorization token for a session

        Returns:
            str: Random token
        """
        return secrets.token_urlsafe(TOKEN_BYTES)

    