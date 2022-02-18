# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import api_pb2 as api__pb2


class ShortenerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.shortenURL = channel.unary_unary(
                '/main.Shortener/shortenURL',
                request_serializer=api__pb2.shortenURLRequest.SerializeToString,
                response_deserializer=api__pb2.shortenURLResponse.FromString,
                )


class ShortenerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def shortenURL(self, request, context):
        """shortenURL takes url and slug(optional) for request
        and returns url and slug in response
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ShortenerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'shortenURL': grpc.unary_unary_rpc_method_handler(
                    servicer.shortenURL,
                    request_deserializer=api__pb2.shortenURLRequest.FromString,
                    response_serializer=api__pb2.shortenURLResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'main.Shortener', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Shortener(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def shortenURL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/main.Shortener/shortenURL',
            api__pb2.shortenURLRequest.SerializeToString,
            api__pb2.shortenURLResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DatabaseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.checkIfPresent = channel.unary_unary(
                '/main.Database/checkIfPresent',
                request_serializer=api__pb2.checkIfPresentRequest.SerializeToString,
                response_deserializer=api__pb2.checkIfPresentResponse.FromString,
                )
        self.storeInDB = channel.unary_unary(
                '/main.Database/storeInDB',
                request_serializer=api__pb2.storeInDBRequest.SerializeToString,
                response_deserializer=api__pb2.storeInDBResponse.FromString,
                )


class DatabaseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def checkIfPresent(self, request, context):
        """checkIfPresent checks if slug is already present in DB
        takes slug as request and returns bool as response
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def storeInDB(self, request, context):
        """storeInDB stores in Database
        takes url and slug in request and returns Status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatabaseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'checkIfPresent': grpc.unary_unary_rpc_method_handler(
                    servicer.checkIfPresent,
                    request_deserializer=api__pb2.checkIfPresentRequest.FromString,
                    response_serializer=api__pb2.checkIfPresentResponse.SerializeToString,
            ),
            'storeInDB': grpc.unary_unary_rpc_method_handler(
                    servicer.storeInDB,
                    request_deserializer=api__pb2.storeInDBRequest.FromString,
                    response_serializer=api__pb2.storeInDBResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'main.Database', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Database(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def checkIfPresent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/main.Database/checkIfPresent',
            api__pb2.checkIfPresentRequest.SerializeToString,
            api__pb2.checkIfPresentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def storeInDB(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/main.Database/storeInDB',
            api__pb2.storeInDBRequest.SerializeToString,
            api__pb2.storeInDBResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
