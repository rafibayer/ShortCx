import grpc
import apiservice_pb2
import authservice_pb2
import authservice_pb2_grpc
import unittest

# Address for TEST/LOCAL service
SERVICE_ADDR = "localhost:9091"

class TestApiService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        channel = grpc.insecure_channel(target=SERVICE_ADDR)
        cls.stub = authservice_pb2_grpc.AuthServiceStub(channel)

    def test_BadLogin(self):
        request = apiservice_pb2.LoginRequest(email="fake@example.com", password="fakepassword")
        try:
            resp = self.stub.Login(request)
        except grpc.RpcError as e:
           self.assertEqual(e.code(), grpc.StatusCode.PERMISSION_DENIED)

    def test_BadLogout(self):
        request = apiservice_pb2.LogoutRequest(auth_token="FAKE TOKEN")
        try:
            resp = self.stub.Logout(request)
        except grpc.RpcError as e:
            self.assertEqual(e.code(), grpc.StatusCode.NOT_FOUND)


if __name__ == '__main__':
    unittest.main()