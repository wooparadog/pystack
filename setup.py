# !/usr/bin/env python

from setuptools import setup

setup(
    name='pystack',
    version='0.6',
    description='Tool to print python thread and greenlet stacks',
    author="Haochuan Guo",
    author_email='guohaochuan@gmail.com',
    py_modules=['pystack'],
    url='https://github.com/wooparadog/pystack/',
    entry_points={
        'console_scripts': [
            ['pystack = pystack:main'],
        ],
    },
    install_requires=[
        'click>=5.1,<6.0',
    ],
)
