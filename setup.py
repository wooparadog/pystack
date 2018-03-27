# !/usr/bin/env python

from setuptools import setup

setup(
    name='pystack',
    version='0.6',
    description='Tool to print python thread and greenlet stacks',
    long_description=open('README.md').read(),
    author='Haochuan Guo',
    author_email='guohaochuan@gmail.com',
    py_modules=['pystack'],
    zip_safe=False,
    url='https://github.com/wooparadog/pystack/',
    keywords=['pystack', 'pstack', 'jstack', 'gdb', 'lldb', 'greenlet'],
    entry_points={
        'console_scripts': [
            ['pystack = pystack:main'],
        ],
    },
    install_requires=[
        'click>=5.1,<6.0',
    ],
    platforms=['Any'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Utilities',
    ],
)
