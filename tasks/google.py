# -*- coding: utf-8 -*-
from urllib import quote_plus


def process_command(user_input, **kwargs):
    if len(user_input) < 3:
        return 'Usage: Igor google <term>'
    else:
        return 'http://google.co.uk/?q=%s' % (quote_plus(user_input[2]))
