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
        cls.stub = apiservice_pb2_grpc.APIServiceStub(grpc.insecure_channel(target=SERVICE_ADDR))

    @staticmethod
    def _randname():
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

    def makeAcc(self, username="TESTUSER", password="TESTPASSWORD"):
        request = apiservice_pb2.CreateUserRequest(username=username, password=password, password_conf=password)
        return self.stub.CreateUser(request).auth_token

    def makeSess(self, username="TESTUSER", password="TESTPASSWORD"):
        request = apiservice_pb2.LoginRequest(username=username, password=password)
        return self.stub.Login(request).auth_token

    def makeShort(self, token, target="example.com"):
        request = apiservice_pb2.CreateShortcutRequest(auth_token = token, target_url = target)
        return self.stub.CreateShortcut(request).url_token

    def test_CreateUser(self):
        self.makeAcc(username=self._randname())

    def test_GetSession(self):
        name = self._randname()
        token = self.makeAcc(name)
        request = apiservice_pb2.GetSessionRequest(auth_token = token)
        self.assertEqual(self.stub.GetSession(request).username, name) 

    def test_Login(self):
        name, password = self._randname(), "PASSWORD"
        self.makeAcc(name, password)
        request = apiservice_pb2.LoginRequest(username=name, password=password)
        resp = self.stub.Login(request)

    def test_Logout(self):
        token = self.makeAcc(self._randname())
        request = apiservice_pb2.LogoutRequest(auth_token=token)

    def test_CreateShortcut(self):
        token = self.makeAcc(self._randname())
        self.makeShort(token)

    def test_DeleteShortcut(self):
        token = self.makeAcc(self._randname())
        urlTok = self.makeShort(token)
        req = apiservice_pb2.DeleteShortcutRequest(auth_token = token, url_token = urlTok)
        self.stub.DeleteShortcut(req)

    def test_GetShortcut(self):
        token = self.makeAcc(self._randname())
        urlTok = self.makeShort(token)
        req = apiservice_pb2.GetShortcutRequest(url_token = urlTok)
        self.stub.GetShortcut(req)

    def test_GetAllShortcuts(self):
        token = self.makeSess("rafi", "mypassword")
        req = apiservice_pb2.GetAllShortcutsRequest(auth_token = token)
        self.stub.GetAllShortcuts(req)

if __name__ == "__main__":
    unittest.main()


