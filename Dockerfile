# Dockerfile client
FROM 10.72.32.88:8083/python/python3.8-teb-base:dvc-test
MAINTAINER Bilge Sipal Sert
USER root
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
#RUN python -m grpc_tools.protoc -I./protobufs --python_out=. --pyi_out=. \
#    --grpc_python_out=. protobufs/greet.proto

EXPOSE 5000
ENV FLASK_APP=client.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]