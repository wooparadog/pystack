#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import tempfile

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


def print_stack(pid, include_greenlet=False, verbose=False):
    """Executes a file in a running Python process."""
    tmp_file = tempfile.mktemp()
    commands = []
    commands.append(FILE_OPEN_COMMAND)
    commands.extend(THREAD_STACK_COMMANDS)
    if include_greenlet:
        commands.extend(GREENLET_STACK_COMMANDS)
    commands.append(FILE_CLOSE_COMMAND)
    command = r';'.join(commands)

    gdb_cmds = [
        'PyGILState_Ensure()',
        'PyRun_SimpleString("exec(\\"%s\\")")' % (
            command % tmp_file
            ),
        'PyGILState_Release($1)',
        ]
    cmd = 'gdb -p %d -batch %s' % (
        pid, ' '.join(["-eval-command='call %s'" % cmd for cmd in gdb_cmds])
        )
    process = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if verbose:
        print out
        print err
    with open(tmp_file) as fo:
        print fo.read()


@click.command()
@click.argument('pid', required=True, type=int)
@click.option('--include-greenlet', default=False, is_flag=True,
              help="Also print greenlet stacks")
@click.option('-v', '--verbose', default=False, is_flag=True,
              help="Verbosely print error and warnings")
def stack(pid, include_greenlet, verbose):
    '''Print stack of python process.

    $ pystack <pid>
    '''
    return print_stack(pid, include_greenlet, verbose)

if __name__ == '__main__':
    stack()
