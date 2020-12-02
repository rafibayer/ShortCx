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
        # print("done")

    def _randname(self):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(8))


    def test_CreateUser(self):
        request = apiservice_pb2.CreateUserRequest(
            username=self._randname(),
            password="testpassword",
            password_conf="testpassword")

        print(request)

        # print("calling create")
        resp = self.stub.CreateUser(request)
        print(resp)
        #self.assertRaises(grpc.RpcError, self.stub.CreateUser, request)

    # def test_Login(self):
    #     request = apiservice_pb2.LoginRequest(
    #         username="wbanhrzp",
    #         password="testpassword")
        
    #     # print("calling login")
    #     resp = self.stub.Login(request)
    #     print(resp)
    #     # self.assertRaises(grpc.RpcError, self.stub.Login, request)


    # def test_Logout(self):
    #     request = apiservice_pb2.LogoutRequest(
    #         auth_token="FAKE TOKEN")
        
    #     # print("calling logout")
        # self.assertRaises(grpc.RpcError, self.stub.Logout, request)

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


