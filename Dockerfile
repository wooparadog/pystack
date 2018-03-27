FROM ubuntu:xenial

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y python python-dbg python-tox gdb && \
    rm -rf /var/lib/apt/lists/*
ADD . /pystack
WORKDIR /pystack

CMD ["tox"]
