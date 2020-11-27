from controller import Controller
from datastore import DataStore
from sessionstore import SessionStore
from concurrent import futures
import logging
import grpc
import authservice_pb2
import authservice_pb2_grpc
import os

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s')


class AuthService(authservice_pb2_grpc.AuthServiceServicer):

    def __init__(self, auth_controller):
        super().__init__()
        self.auth_controller = auth_controller

    def Login(self, request, context):
        return authservice_pb2.LoginResponse(auth_token="FAKE TOKEN")

    def Logout(self, request, context):
        return authservice_pb2.LoginResponse(success=True)

def serve(port, workers, service):
    logging.info(f'AuthService starting @{PORT} with {WORKERS} workers')
    server = grpc.server(futures.ThreadPoolExecutor(workers))
    authservice_pb2_grpc.add_AuthServiceServicer_to_server(service, server)
    server.add_insecure_port(port)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    # AuthService
    PORT = f"[::]:{os.getenv('PORT')}"
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

    # Initialize DataStore, Controller, and Service
    data_store = DataStore(DB_HOST, DB_USER, DB_PASS, DB_NAME)
    session_store = SessionStore(REDIS_HOST, REDIS_PORT, REDIS_MAX_CON)
    auth_service = AuthService(Controller(data_store, session_store))
    serve(PORT, WORKERS, auth_service)

