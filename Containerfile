FROM quay.io/fedora/fedora:37

RUN dnf install -y --setopt=install_weak_deps=False \
        python2.7 \
        python3.6 \
        python3.7 \
        python3.8 \
        python3.9 \
        python3.10 \
        python3.11 \
        python3.12 \
        tox \
        gdb \
        lldb \
        which \
        less \
        procps-ng \
        strace && \
    dnf clean all
WORKDIR /pystack

CMD ["tox"]
