# !/usr/bin/env python

from setuptools import setup

setup(
    name='pstack',
    version='0.6',
    description='Tool to print python thread and greenlet stacks',
    author="Haochuan Guo",
    author_email='guohaochuan@gmail.com',
    py_modules=['stack'],
    url='https://github.com/wooparadog/pstack/',
    entry_points={
        'console_scripts': [
            ['pstack = stack:stack'],
        ],
    },
    install_requires=[
        'click>=5.1,<6.0',
    ],
)
