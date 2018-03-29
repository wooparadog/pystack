[![PyPI](https://img.shields.io/pypi/v/pystack-debugger.svg)](https://pypi.org/project/pystack-debugger/)

# pystack

The pystack is to python as jstack is to java.

It's a debug tool to print python threads or greenlet stacks.

Idea stolen from [pyrasite](https://github.com/lmacken/pyrasite).

## Install

    $ pip install pystack-debugger

## Usage

You may need to run it with `sudo`.

    $ sudo pystack [--include-greenlet] <pid>

## Compatibility

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pystack-debugger.svg)](https://pypi.org/project/pystack-debugger/)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/pystack-debugger.svg)](https://pypi.org/project/pystack-debugger/)

The pystack is compatible with CPython 2.7+ and CPython 3.6+ in both client
(the debugger) and server (the destination process).

Using PyPy may work in client (the debugger) but it is untested. Do not attempt
to attach a PyPI process as destination since the pystack debugger uses gdb/lldb
to invoke the CPython ABI.
