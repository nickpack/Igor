# -*- coding: utf-8 -*-
def process_command(user_input, **kwargs):
    try:
        return '(mooning) FU %s, you\'re doing it wrong. (mooning)' % user_input[2]
    except Exception:
        return 'Please forgive my insolence.'