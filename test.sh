#!/usr/bin/env sh
set -e
OCI_NAME=ghcr.io/wooparadog/pystack:test
podman build -t "$OCI_NAME" "$PWD"
podman run -it --rm --cap-add SYS_PTRACE -v "$PWD:/pystack" "$OCI_NAME" "${@}"
