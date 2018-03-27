# pystack

## IMPORTANT NOTICE

This is the last release using the `pstack` project name in PyPI.

Please use `pystack-debugger` in future. (e.g. `pip install pystack-debugger`)

See also https://pypi.python.org/pypi/pystack-debugger.

## Introduction

pystack is to python as jstack is to java!

It's a debug tool to print python threads or greenlet stacks.

Idea stolen from [pyrasite](https://github.com/lmacken/pyrasite)

## Install

```
$ pip install pystack-debugger
```

## Usage

You may need to run it with `sudo`.

```
$ sudo pystack <pid> [--include-greenlet]
```
