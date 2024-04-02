#serve.py
from concurrent import futures
import grpc
import os
import socket


print(socket.gethostbyname(socket.gethostname()))
import grpc
from greet_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server
from greet_pb2 import HelloReply


class Greeter(GreeterServicer):
    def SayHello(self, request, context):
        return HelloReply(message=f"Hello, {request.name}")

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

    if os.path.isfile('server.key'):
        print('secure')
        with open("server.key", "rb") as fp:
            server_key = fp.read()
        with open("server.pem", "rb") as fp:
            server_cert = fp.read()
        with open("ca.pem", "rb") as fp:
            ca_cert = fp.read()
        server_credentials = grpc.ssl_server_credentials(
            [(server_key, server_cert)],
            root_certificates=ca_cert,
            require_client_auth=True,
        )

        server.add_secure_port('[::]:443' , server_credentials)
    else:
        print('insecure')
        server.add_insecure_port('[::]:50051')
        print('server', server)

    add_GreeterServicer_to_server(Greeter(), server)
    print(GreeterServicer)
    #SERVICE_NAMES=()
    server.start()
    server.wait_for_termination()
    return

if __name__ == '__main__':
    server()