FROM ubuntu:bionic

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y \
        python2.7 python2.7-dbg \
        python3.6 python3.6-dbg \
        tox gdb lldb strace && \
    rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/lldb-6.0 /usr/bin/lldb
ADD . /pystack
WORKDIR /pystack

CMD ["tox"]
