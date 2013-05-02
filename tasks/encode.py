# -*- coding: utf-8 -*-
import base64
import urllib


def process_command(user_input, **kwargs):
    if len(user_input) < 4:
        return 'Usage: Igor encode <base64|url|hex> <string>'

    try:
        encoded = ''
        if user_input[2] == 'base64':
            encoded = base64.b64encode(user_input[3])
        elif user_input[2] == 'url':
            encoded = urllib.quote_plus(user_input[3])
        elif user_input[2] == 'hex':
            encoded = user_input[3].encode('hex')

        return 'Encoded string: %s' % encoded
    except Exception, e:
        return 'Unable to encode the provided string: %s' % e.message
