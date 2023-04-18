FROM amazonlinux:latest

RUN yum install -y yum gcc openssl-devel bzip2-devel libffi-devel wget tar gzip
RUN yum groupinstall -y "Development Tools"
RUN wget https://www.python.org/ftp/python/3.9.16/Python-3.9.16.tgz
RUN tar -xzf Python-3.9.16.tgz
RUN cd Python-3.9.16
RUN ls -latr
RUN pwd
RUN cd Python-3.9.16 && ./configure --enable-optimizations && make altinstall
RUN rm -f /opt/Python-3.9.16.tgz
RUN python3.9 -V
RUN /usr/local/bin/python3.9 -m pip install --upgrade pip

COPY ./src/ /src
WORKDIR /src

RUN pip3 install boto3 openai -t .
RUN mkdir python && mv * python/ || true
CMD ["zip", "-r", "/var/task/layer.zip", "."]
