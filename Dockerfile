# Dockerfile serve
FROM 10.72.32.88:8083/python/python3.8-teb-base:dvc-test
MAINTAINER Bilge Sipal Sert
USER root
WORKDIR /app
#RUN mkdir /service
#COPY serve  /service/serve/
#COPY protobufs/ /service/serve/protobufs/
#COPY ca.pem /service/serve/
#WORKDIR /service/serve
COPY . .
RUN pip install -r requirements.txt
#RUN python -m grpc_tools.protoc -I./protobufs --python_out=. \
#           --grpc_python_out=. protobufs/greet.proto

#RUN openssl req -newkey rsa:4096\
#         -nodes -keyout server.key \
#    -x509 -days 365 -out server.csr \
#    -subj "CN=serve.nlp-colc.apps.ocpdt.int.teb.com.tr"
#
# RUN --mount=type=secret,id=ca.key \
#     openssl x509 -req -in server.csr -CA ca.pem -CAkey /run/secrets/ca.key \
#                  -set_serial 1 -out server.pem
USER 1001
EXPOSE 50051
ENTRYPOINT [ "python", "serve.py" ]