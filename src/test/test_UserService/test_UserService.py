import grpc
import apiservice_pb2
import userservice_pb2
import userservice_pb2_grpc

import unittest

# Address for TEST/LOCAL service
SERVICE_ADDR = "localhost:9093"

class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        channel = grpc.insecure_channel(target=SERVICE_ADDR)
        cls.stub = userservice_pb2_grpc.UserServiceStub(channel)

    def test_CreateUser(self):
        request = apiservice_pb2.CreateUserRequest(
            email = "fake@example.com",
            username = "fakeuser",
            password = "fakepassword",
            password_conf = "fakepassword"
        )
        resp = self.stub.CreateUser(request)
        print(resp)

if __name__ == "__main__":
    unittest.main()