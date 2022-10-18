FROM quay.io/fedora/fedora:37

RUN dnf install -y --setopt=install_weak_deps=False \
        python2.7 \
        python3.6 \
        python3.7 \
        python3.8 \
        python3.9 \
        python3.10 \
        tox \
        gdb \
        lldb \
        strace && \
    dnf clean all
ADD . /pystack
WORKDIR /pystack

CMD ["tox"]
