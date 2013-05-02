# -*- coding: utf-8 -*-
from random import choice
import string


def process_command(user_input, **kwargs):
    if len(user_input) < 3:
        return 'Usage: Igor passwordgenerator <length>'

    if not user_input[2].isdigit():
        return 'You need to give me a number for the length'

    length = int(user_input[2])

    password = ''.join(
        [choice(string.letters + string.digits) for i in range(length)])

    return 'Random Password: %s' % password