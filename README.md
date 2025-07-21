[![PyPI](https://img.shields.io/pypi/v/pystack-debugger.svg)](https://pypi.org/project/pystack-debugger/)

# pystack-debugger

The pystack-debugger is to python as jstack is to java.

It's a debug tool to print python threads or greenlet stacks.

Idea stolen from [pyrasite](https://github.com/lmacken/pyrasite).

## Requirements

- **Python 3.8+** (CPython implementation)
- **Debugger**: Either `gdb` (Linux) or `lldb` (macOS/Linux)
- **Privileges**: Root access (`sudo`) to attach to other processes

**Note**: On some Linux systems, you may need to adjust the `ptrace_scope` setting to allow debugger attachment.

## Install

    $ pip install pystack-debugger

## Usage

You may need to run it with `sudo`.

    $ sudo pystack [--include-greenlet] <pid>

## Compatibility

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pystack-debugger.svg)](https://pypi.org/project/pystack-debugger/)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/pystack-debugger.svg)](https://pypi.org/project/pystack-debugger/)

The pystack is compatible with CPython 3.8+ in both client side (the debugger)
and server side (the destination process).

Using PyPy may work in client side (the debugger) but it is untested. Do not
attempt to attach a PyPy process as destination. It may lead to unexpected and
undefined behavior, because the pystack debugger uses gdb/lldb to invoke the
CPython ABI.

## Development

Run testing on a container environment:

    $ podman machine start
    $ ./test.sh
    $ ./test.sh coverage html
