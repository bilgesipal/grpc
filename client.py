
#client.py
import os
import grpc


from flask import Flask
from flask_cors import CORS
from flask import Flask, Response
app = Flask('GRPC_CHECK')
CORS(app)
from greet_pb2_grpc import GreeterStub
from greet_pb2 import HelloRequest



#host = os.getenv("HOST")
host = '10.200.34.112'
print('host', host)

@app.after_request
def security(response: Response) -> Response:
    """
    Overwrites critical information before sending the response

    Args:
        response (Response): Response object

    Returns:
        Response: Response object
    """
    response.headers["X-XXS-Protection"] = "1; mode=block"
    response.headers["Servers"] = "AAAA"
    return response


if os.path.isfile('client.key'):
    print('secure')
    with open("client.key", "rb") as fp:
        client_key = fp.read()
    with open("client.pem", "rb") as fp:
        client_cert = fp.read()
    with open("ca.pem", "rb") as fp:
        ca_cert = fp.read()
    creds = grpc.ssl_channel_credentials(ca_cert, client_key, client_cert)
    channel = grpc.secure_channel(
        f"{host}:443", creds
    )

else:
    print('insecure')
    channel = grpc.insecure_channel(
     f"{host}:50051"
    )

stub = GreeterStub(channel)

# response = stub.SayHello(HelloRequest(name='Bilge'))
# print("Greeter client received: " + response.message)
# response = stub.SayHello(HelloRequest(name='Bilge'))
# print("Greeter client received: " + response.message)

@app.route('/')
def get_name():

    try:
        request = HelloRequest(name='Bilge')
        response = stub.SayHello(request)
        print("Greeter client received: " + response.message)
        response = stub.SayHello(HelloRequest(name='Bilge'))
        print("Greeter client received: " + response.message)
        return response.message
    except(grpc._channel._InactiveRpcError):
        return 'serve gRPC çalışmıyor'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False,threaded=True)