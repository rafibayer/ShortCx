import grpc
from . import apiservice_pb2
from . import apiservice_pb2_grpc
import unittest

SERVICE_ADDR = "localhost:9090"

def LogName(func):

    def inner(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return inner

class TestApiService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        channel = grpc.insecure_channel(target=SERVICE_ADDR)
        cls.stub = apiservice_pb2_grpc.APIServiceStub(channel)

    def test_CreateUser(self):
        request = apiservice_pb2.CreateUserRequest(
            email="test@example.com",
            username="testuser",
            password="testpassword",
            password_conf="testpassword")
        
        resp = self.stub.CreateUser(request)

    def test_Login(self):
        request = apiservice_pb2.LoginRequest(
            email="test@example.com",
            password="testpassword")
        
        resp = self.stub.Login(request)

    def test_Logout(self):
        request = apiservice_pb2.LogoutRequest(
            auth_token="FAKE TOKEN")
        
        resp = self.stub.Logout(request)

    def test_CreateShortcut(self):
        request = apiservice_pb2.CreateShortcutRequest(
            auth_token="FAKE TOKEN",
            target_url="FAKE URL")
        
        resp = self.stub.CreateShortcut(request)

    def test_DeleteShortcut(self):
        request = apiservice_pb2.DeleteShortcutRequest(
            auth_token="FAKE TOKEN",
            url_token="FAKE TOKEN")
        
        resp = self.stub.DeleteShortcut(request)

    def test_GetShortcut(self):
        request = apiservice_pb2.GetShortcutRequest(
            url_token="FAKE TOKEN")
        
        resp = self.stub.GetShortcut(request)

if __name__ == "__main__":
    unittest.main()


