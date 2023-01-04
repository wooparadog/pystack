# !/usr/bin/env python

from setuptools import setup

setup(
    name='pystack-debugger',
    version='0.10.0',
    description='Tool to print python thread and greenlet stacks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Haochuan Guo',
    author_email='guohaochuan@gmail.com',
    maintainer='Jiangge Zhang',
    maintainer_email='tonyseek@gmail.com',
    py_modules=['pystack'],
    zip_safe=False,
    license='MIT',
    url='https://github.com/wooparadog/pystack/',
    keywords=['pystack', 'pstack', 'jstack', 'gdb', 'lldb', 'greenlet'],
    entry_points={
        'console_scripts': [
            'pystack = pystack:main',
        ],
    },
    install_requires=[
        'click>=5.1,<6.0',
    ],
    setup_requires=[
        'setuptools>=38.6.0',
    ],
    platforms=['linux', 'darwin'],
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Utilities',
    ],
)
