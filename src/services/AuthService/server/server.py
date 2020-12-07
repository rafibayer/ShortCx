from controller import Controller
from datastore import DataStore
from sessionstore import SessionStore
from concurrent import futures
import exceptions
import logging
import grpc
import apiservice_pb2
import authservice_pb2
import authservice_pb2_grpc
import os

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s')

class AuthService(authservice_pb2_grpc.AuthServiceServicer):

    def __init__(self, auth_controller: Controller):
        """Creates a new AuthService object

        Args:
            auth_controller (Controller): Auth controller
        """
        super().__init__()
        self.auth_controller = auth_controller

    def GetSession(self, request: apiservice_pb2.GetSessionRequest, context: grpc.RpcContext) -> apiservice_pb2.GetSessionResponse:
        """Handles GetSession Rpc

        Args:
            request (apiservice_pb2.GetSessionRequest): User GetSessionRequest forwarded from ApiService
            context (grpc.RpcContext): Request Context

        Returns:
            apiservice_pb2.GetSessionResponse: response containing session state or error details
        """
        try:
            return self.auth_controller.get_session(request)
        except exceptions.AuthException as e:
            context.set_details(e.message)
            context.set_code(e.status_code)
            return apiservice_pb2.GetSessionResponse()

    def Login(self, request: apiservice_pb2.LoginRequest, context: grpc.RpcContext) -> apiservice_pb2.LoginResponse:
        """Handles Login RPC

        Args:
            request (LoginRequest): User login request forwarded from ApiService
            context (grpc.RpcContext): Request context

        Returns:
            LoginResponse: response containing auth_token or error details
        """
        try:
            return self.auth_controller.login(request)
        except exceptions.AuthException as e:
            context.set_details(e.message)
            context.set_code(e.status_code)
            return apiservice_pb2.LoginResponse()

    def Logout(self, request: apiservice_pb2.LogoutRequest, context: grpc.RpcContext) -> apiservice_pb2.LogoutResponse:
        """Handles Logout RPC

        Args:
            request (LogoutRequest): User logout request forwarded from ApiService
            context (grpc.RpcContext): Request context

        Returns:
            LogoutResponse: Response containing success message or error details
        """
        try:
            return self.auth_controller.logout(request)
        except exceptions.AuthException as e:
            context.set_details(e.message)
            context.set_code(e.status_code)
            return apiservice_pb2.LogoutResponse()

def serve(port: str, workers: int, service: AuthService):
    """Serves AuthService

    Args:
        port (str): Port/host '[::]:<PORT>'
        workers (int): Number of threadpool workers
        service (AuthService): AuthService instance
    """
    logging.info(f'AuthService starting @{PORT} with {WORKERS} workers')
    server = grpc.server(futures.ThreadPoolExecutor(workers))
    authservice_pb2_grpc.add_AuthServiceServicer_to_server(service, server)
    server.add_insecure_port(port)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    """Entrypoint for server, collects environment details and serves
    """
    # AuthService
    PORT = f"[::]{os.getenv('PORT')}"
    WORKERS = int(os.getenv('WORKERS'))

    # DataStore access
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_NAME = os.getenv('DB_NAME')

    # SessionStore Access
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')
    REDIS_MAX_CON = int(os.getenv('REDIS_MAX_CON'))

    # Initialize DataStore, SessionStore, Controller, and Service
    data_store = DataStore(DB_HOST, DB_USER, DB_PASS, DB_NAME)
    session_store = SessionStore(REDIS_HOST, REDIS_PORT, REDIS_MAX_CON)
    auth_service = AuthService(Controller(data_store, session_store))
    serve(PORT, WORKERS, auth_service)