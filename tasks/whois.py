# -*- coding: utf-8 -*-
from whoislookup import WhoisLookup


def process_command(user_input, **kwargs):

    if len(user_input) < 3:
        return 'Usage: Igor whois <domain name>'

    try:
        domain = WhoisLookup(user_input[2])
    except Exception, e:
        return 'Error encountered during whois: %s' % e.message

    if hasattr(domain, 'expiry_date'):
        return 'Registered domain expires on: %s' % domain.expiry_date
    else:
        return 'Domain appears to be unregistered.'