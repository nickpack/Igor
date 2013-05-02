# -*- coding: utf-8 -*-
import imp
import os
#MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')
MODULE_EXTENSIONS = ('.py')


def process_command(user_input, **kwargs):
    file, pathname, description = imp.find_module('tasks')
    if file:
        raise ImportError('Not a package: %r', 'tasks')
        # Use a set because some may be both source and compiled.
    commands = set([os.path.splitext(module)[0]
                    for module in os.listdir(pathname)
                    if module.endswith(MODULE_EXTENSIONS)])
    commands.remove('__init__')
    output_commands = ', '.join(commands)

    return 'Supported Commands: %s' % output_commands