import grpc
import apiservice_pb2
import apiservice_pb2_grpc
import unittest
import string
import random

SERVICE_ADDR = "localhost:9090"


class TestApiService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # print("establishing stub")
        channel = grpc.insecure_channel(target=SERVICE_ADDR)
        cls.stub = apiservice_pb2_grpc.APIServiceStub(channel)
        cls.username = cls._randname()
        cls.tokens = set()

    @staticmethod
    def _randname():
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

    def test_CreateUser(self):
        request = apiservice_pb2.CreateUserRequest(
            username=self.username,
            password="testpassword",
            password_conf="testpassword")

        resp = self.stub.CreateUser(request)
        self.tokens.append(resp.auth_token)

    def test_Login(self):
        request = apiservice_pb2.LoginRequest(
            username=self.username,
            password="testpassword")
        
        resp = self.stub.Login(request)
        self.tokens.append(resp.auth_token)

    def test_Logout(self):
        for token in self.tokens:
            request = apiservice_pb2.LogoutRequest(
                auth_token=token)
            
            self.stub.Logout(request)

    # def test_CreateShortcut(self):
    #     request = apiservice_pb2.CreateShortcutRequest(
    #         auth_token="FAKE TOKEN",
    #         target_url="FAKE URL")
        
    #     # print("calling createshortcut")
    #     resp = self.stub.CreateShortcut(request)

    # def test_DeleteShortcut(self):
    #     request = apiservice_pb2.DeleteShortcutRequest(
    #         auth_token="FAKE TOKEN",
    #         url_token="FAKE TOKEN")
        
    #     # print("calling deleteshortcut")
    #     resp = self.stub.DeleteShortcut(request)

    # def test_GetShortcut(self):
    #     request = apiservice_pb2.GetShortcutRequest(
    #         url_token="FAKE TOKEN")
        
    #     # print("calling getshortcut")
    #     resp = self.stub.GetShortcut(request)

if __name__ == "__main__":
    unittest.main()


