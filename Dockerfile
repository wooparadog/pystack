FROM ubuntu:bionic

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y \
        python2.7 python3.6 tox gdb lldb strace && \
    ln -s /usr/bin/lldb-6.0 /usr/bin/lldb && \
    rm -rf /var/lib/apt/lists/*
ADD . /pystack
WORKDIR /pystack

CMD ["tox"]
