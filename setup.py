# !/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


entry_points = ["pstack = stack:stack"]


setup(
    name="pstack",
    version='0.5',
    description="Tool to print python thread and greenlet stacks",
    author="Haochuan Guo",
    author_email="guohaochuan@gmail.com",
    py_modules=['stack'],
    url="https://github.com/wooparadog/pstack/",
    entry_points={"console_scripts": entry_points},
    install_requires=[
        'click==5.1',
    ],
)
