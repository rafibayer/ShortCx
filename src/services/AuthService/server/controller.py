import bcrypt
import exceptions
import apiservice_pb2

STR_ENCODING = 'utf-8'

class Controller:

    def __init__(self, datastore, sessionstore):
        self.datastore = datastore
        self.sessionstore = sessionstore

    def login(self, loginRequest):
        if self.authenticate(loginRequest.email, loginRequest.password):
            token = self.sessionstore.create_session(loginRequest.email)
            return apiservice_pb2.LoginResponce(auth_token=token)
        raise exceptions.BadCredentialsError()

    def logout(self, logoutRequest):
        self.sessionstore.end_session(logoutRequest.auth_token)
        return apiservice_pb2.LogoutResponse(success=True)

    def authenticate(self, email, password):
        try:
            expected = bytes(self.datastore.get_credentials(email), encoding=STR_ENCODING)
        except exceptions.AuthException:
            return False

        given = bytes(password, encoding=STR_ENCODING)
        return bcrpyt.checkpw(given, expected)
        

