# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import apiservice_pb2 as apiservice__pb2


class APIServiceStub(object):
    """API Service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/protos.APIService/CreateUser',
                request_serializer=apiservice__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=apiservice__pb2.CreateUserResponse.FromString,
                )
        self.Login = channel.unary_unary(
                '/protos.APIService/Login',
                request_serializer=apiservice__pb2.LoginRequest.SerializeToString,
                response_deserializer=apiservice__pb2.LoginResponse.FromString,
                )
        self.Logout = channel.unary_unary(
                '/protos.APIService/Logout',
                request_serializer=apiservice__pb2.LogoutRequest.SerializeToString,
                response_deserializer=apiservice__pb2.LogoutResponse.FromString,
                )
        self.CreateShortcut = channel.unary_unary(
                '/protos.APIService/CreateShortcut',
                request_serializer=apiservice__pb2.CreateShortcutRequest.SerializeToString,
                response_deserializer=apiservice__pb2.CreateShortcutResponse.FromString,
                )
        self.DeleteShortcut = channel.unary_unary(
                '/protos.APIService/DeleteShortcut',
                request_serializer=apiservice__pb2.DeleteShortcutRequest.SerializeToString,
                response_deserializer=apiservice__pb2.DeleteShortcutResponse.FromString,
                )
        self.GetShortcut = channel.unary_unary(
                '/protos.APIService/GetShortcut',
                request_serializer=apiservice__pb2.GetShortcutRequest.SerializeToString,
                response_deserializer=apiservice__pb2.GetShortcutResponse.FromString,
                )


class APIServiceServicer(object):
    """API Service definition
    """

    def CreateUser(self, request, context):
        """Create a new user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Login to an existing account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Logout(self, request, context):
        """Logout request for existing session
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateShortcut(self, request, context):
        """Create new shortcut
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteShortcut(self, request, context):
        """Delete existing shortcut
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetShortcut(self, request, context):
        """Get url of existing shortcut
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_APIServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=apiservice__pb2.CreateUserRequest.FromString,
                    response_serializer=apiservice__pb2.CreateUserResponse.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=apiservice__pb2.LoginRequest.FromString,
                    response_serializer=apiservice__pb2.LoginResponse.SerializeToString,
            ),
            'Logout': grpc.unary_unary_rpc_method_handler(
                    servicer.Logout,
                    request_deserializer=apiservice__pb2.LogoutRequest.FromString,
                    response_serializer=apiservice__pb2.LogoutResponse.SerializeToString,
            ),
            'CreateShortcut': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateShortcut,
                    request_deserializer=apiservice__pb2.CreateShortcutRequest.FromString,
                    response_serializer=apiservice__pb2.CreateShortcutResponse.SerializeToString,
            ),
            'DeleteShortcut': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteShortcut,
                    request_deserializer=apiservice__pb2.DeleteShortcutRequest.FromString,
                    response_serializer=apiservice__pb2.DeleteShortcutResponse.SerializeToString,
            ),
            'GetShortcut': grpc.unary_unary_rpc_method_handler(
                    servicer.GetShortcut,
                    request_deserializer=apiservice__pb2.GetShortcutRequest.FromString,
                    response_serializer=apiservice__pb2.GetShortcutResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.APIService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class APIService(object):
    """API Service definition
    """

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.APIService/CreateUser',
            apiservice__pb2.CreateUserRequest.SerializeToString,
            apiservice__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.APIService/Login',
            apiservice__pb2.LoginRequest.SerializeToString,
            apiservice__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Logout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.APIService/Logout',
            apiservice__pb2.LogoutRequest.SerializeToString,
            apiservice__pb2.LogoutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateShortcut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.APIService/CreateShortcut',
            apiservice__pb2.CreateShortcutRequest.SerializeToString,
            apiservice__pb2.CreateShortcutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteShortcut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.APIService/DeleteShortcut',
            apiservice__pb2.DeleteShortcutRequest.SerializeToString,
            apiservice__pb2.DeleteShortcutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetShortcut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.APIService/GetShortcut',
            apiservice__pb2.GetShortcutRequest.SerializeToString,
            apiservice__pb2.GetShortcutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
