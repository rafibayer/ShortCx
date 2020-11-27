from grpc import StatusCode

class AuthException(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class SessionDoesNotExistError(AuthException):
    def __init__(self, message='Session Does Not Exist', status_code=StatusCode.NOT_FOUND):
        super().__init__(message, status_code)

class UserDoesNotExistError(AuthException):
    def __init__(self, message='User Does Not Exist', status_code=StatusCode.NOT_FOUND):
        super().__init__(message, status_code)

class BadCredentialsError(AuthException):
    def __init__(self, message='Invalid Credentials', status_code=StatusCode.PERMISSION_DENIED):
        super().__init__(message, status_code)