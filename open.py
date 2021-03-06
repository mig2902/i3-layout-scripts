#!/usr/bin/env python3

from os.path import isfile
from subprocess import check_output
from sys import argv

from config import LAYOUTS_DIR


def open_layout(layout_name, workspace_number=None):
    executables_file = LAYOUTS_DIR + layout_name
    layout_file = executables_file + '.json'

    if not isfile(layout_file):
        print('layout not found: ' + layout_name)
        return
    if not isfile(executables_file):
        print('executable not found: ' + layout_name)
        return

    if workspace_number:
        check_output(['i3-msg', 'workspace', str(workspace_number)])

    check_output(['i3-msg', 'append_layout', layout_file])
    check_output([executables_file])


if __name__ == '__main__':
    if len(argv) == 3:
        workspace_number = argv[-1]
        try:
            if int(workspace_number) not in range(1, 11):
                raise ValueError
        except ValueError:
            exit(workspace_number + ' is not a valid workspace')

        open_layout(argv[-2], workspace_number)

    elif len(argv) == 2:
        open_layout(argv[-1])

    else:
        exit("usage: open LAYOUT_NAME [WORKSPACE_NUMBER]")
