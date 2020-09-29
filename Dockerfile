FROM lambci/lambda:build-python3.8

ENV AWS_DEFAULT_REGION ap-southeast-2

COPY requirements.txt .

RUN yum install -y wget
