#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import tempfile
import platform

import click


FILE_OPEN_COMMAND = r"f = open(\\\"%s\\\", \\\"w\\\")"
FILE_CLOSE_COMMAND = r"f.close()"

GREENLET_STACK_COMMANDS = [
    r'import gc,greenlet,traceback',
    r"objs=[ob for ob in gc.get_objects() if "
    r"isinstance(ob,greenlet.greenlet) if ob]",
    r"f.write(\\\"\\\\nDumping Greenlets....\\\\n\\\\n\\\\n\\\")",
    r"f.write(\\\"\\\\n---------------\\\\n\\\\n\\\".join("
    r"\\\"\\\".join(traceback.format_stack(o.gr_frame)) for o in objs))",
    ]

THREAD_STACK_COMMANDS = [
    r'import gc,traceback,itertools,sys',
    r"f.write(\\\"Dumping Threads....\\\\n\\\\n\\\\n\\\")",
    r"f.write(\\\"\\\\n---------------\\\\n\\\\n\\\".join("
    r"\\\"\\\".join(traceback.format_stack(o)) for o in "
    r"sys._current_frames().itervalues()))",
    ]


def make_gdb_args(pid, command):
    statements = [
        r'call PyGILState_Ensure()',
        r'call PyRun_SimpleString("exec(\"%s\")")' % command,
        r'call PyGILState_Release($1)',
    ]
    arguments = ['gdb', '-p', str(pid), '-batch']
    arguments.extend("-eval-command='%s'" % s for s in statements)
    return arguments


def make_lldb_args(pid, command):
    statements = [
        r'expr (void *) $gil = (void *) PyGILState_Ensure()',
        r'expr (void) PyRun_SimpleString("exec(\"%s\")")' % command,
        r'expr (void) PyGILState_Release($gil)',
    ]
    arguments = ['lldb', '-p', str(pid), '--batch']
    arguments.extend('--one-line=%s' % s for s in statements)
    return arguments


def print_stack(pid, include_greenlet=False, debugger=None, verbose=False):
    """Executes a file in a running Python process."""
    make_args = make_gdb_args
    environ = dict(os.environ)
    if (
        debugger == 'lldb' or
        (debugger is None and platform.system().lower() == 'darwin')
    ):
        make_args = make_lldb_args
        # fix the PATH environment variable for using built-in Python with lldb
        environ['PATH'] = '/usr/bin:%s' % environ.get('PATH', '')

    tmp_fd, tmp_path = tempfile.mkstemp()
    commands = []
    commands.append(FILE_OPEN_COMMAND)
    commands.extend(THREAD_STACK_COMMANDS)
    if include_greenlet:
        commands.extend(GREENLET_STACK_COMMANDS)
    commands.append(FILE_CLOSE_COMMAND)
    command = r';'.join(commands)

    args = make_args(pid, command % tmp_path)
    process = subprocess.Popen(
        args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=environ)
    out, err = process.communicate()
    if verbose:
        print out
        print err
    print os.read(tmp_fd, 10240)


CONTEXT_SETTINGS = {
    'help_option_names': ['-h', '--help'],
}


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('pid', required=True, type=int)
@click.option('--include-greenlet', default=False, is_flag=True,
              help="Also print greenlet stacks")
@click.option('-d', '--debugger', type=click.Choice(['gdb', 'lldb']))
@click.option('-v', '--verbose', default=False, is_flag=True,
              help="Verbosely print error and warnings")
def stack(pid, include_greenlet, debugger, verbose):
    '''Print stack of python process.

    $ pystack <pid>
    '''
    return print_stack(pid, include_greenlet, debugger, verbose)

if __name__ == '__main__':
    stack()
