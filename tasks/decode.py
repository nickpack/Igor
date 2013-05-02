# -*- coding: utf-8 -*-
import base64
import urllib


def process_command(user_input, **kwargs):
    if len(user_input) < 4:
        return 'Usage: Igor decode <base64|url|hex> <string>'

    try:
        decoded = ''
        if user_input[2] == 'base64':
            decoded = base64.b64decode(user_input[3])
        elif user_input[2] == 'url':
            decoded = urllib.unquote(user_input[3])
        elif user_input[2] == 'hex':
            decoded = user_input[3].decode("hex")

        return 'Decoded String: %s' % decoded
    except Exception, e:
        return 'Unable to decode the provided string: %s' % e.message
