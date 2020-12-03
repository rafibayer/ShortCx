import bcrypt
import exceptions
import apiservice_pb2
import logging

# String encoding to convert between str and bytes
STR_ENCODING = 'utf-8'

class Controller:

    def __init__(self, datastore: 'DataStore', sessionstore: 'SessionStore'):
        """Create a new Controller object

        Args:
            datastore (DataStore): MySQL Database interface
            sessionstore (SessionStore): Redis Session Store interface
        """
        self.datastore = datastore
        self.sessionstore = sessionstore

    def get_session(self, getSessionRequest: apiservice_pb2.GetSessionRequest) -> apiservice_pb2.GetSessionResponse:
        state = self.sessionstore.get_state(getSessionRequest.auth_token)
        return apiservice_pb2.GetSessionResponse(user_id=state.user_id, username=state.username)

    def login(self, loginRequest: apiservice_pb2.LoginRequest) -> apiservice_pb2.LoginResponse:
        """Handles a login request

        Args:
            loginRequest (LoginRequest): User login request forwarded from ApiService

        Raises:
            exceptions.BadCredentialsError: When credentials are invalid

        Returns:
            LoginResponse: response containing auth_token or error details
        """
        user = self.datastore.get_user(loginRequest.username)

        if self.authenticate(user, loginRequest.password):
            token = self.sessionstore.create_session(user.user_id, user.username)
            return apiservice_pb2.LoginResponse(auth_token=token)
        raise exceptions.BadCredentialsError()

    def logout(self, logoutRequest: apiservice_pb2.LogoutRequest) -> apiservice_pb2.LogoutResponse:
        """Handles a logout request

        Args:
            logoutRequest (LogoutRequest): User logout request forwarded from ApiService

        Returns:
            LogoutResponse: response containing success notification or error details
        """
        self.sessionstore.end_session(logoutRequest.auth_token)
        return apiservice_pb2.LogoutResponse(success=True)

    def authenticate(self, user, password: str) -> bool:
        """Authenticates a given username + password

        Args:
            username (User): User details
            password (str): Entered password

        Returns:
            bool: True if valid, false otherwise
        """
        expected = bytes(user.passhash, encoding=STR_ENCODING)
        given = bytes(password, encoding=STR_ENCODING)
        return bcrypt.checkpw(given, expected)
