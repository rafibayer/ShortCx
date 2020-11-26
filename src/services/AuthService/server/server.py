from concurrent import futures
import grpc
import authservice_pb2
import authservice_pb2_grpc
import os

class AuthService(authservice_pb2_grpc.AuthServiceServicer):

    def __init__(self):
        super().__init__()

    def Login(self, request, context):
        return authservice_pb2.LoginResponse(auth_token="FAKE TOKEN")

    def Logout(self, request, context):
        return authservice_pb2.LoginResponse(success=True)

def serve(port, workers):
    print(f'Starting server on port {port} ({workers} workers)')
    server = grpc.server(futures.ThreadPoolExecutor(workers))
    authservice_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port(port)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    PORT = f"[::]:{os.environ.get('PORT', 9091)}"
    WORKERS = int(os.environ.get('WORKERS', 3))
    serve(PORT, WORKERS)

