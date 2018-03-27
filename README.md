# pystack

pystack is to python as jstack is to java!

It's a debug tool to print python threads or greenlet stacks.

Idea stolen from [pyrasite](https://github.com/lmacken/pyrasite)

## Install

```
$ pip install pystack
```

## Usage

You may need to run it with `sudo`.

```
$ sudo pstack <pid> [--include-greenlet]
```
