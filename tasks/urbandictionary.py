# -*- coding: utf-8 -*-
import json
from urllib import quote_plus
from urllib2 import Request, urlopen, HTTPError, URLError

API_URL = 'http://api.urbandictionary.com/v0/define?page=1'


def process_command(user_input, **kwargs):
    if len(user_input) < 3:
        return 'Usage: Igor urbandictionary <term>'

    query = quote_plus(user_input[2])
    req = Request('%s&term=%s' % (API_URL, query))

    try:
        response = urlopen(req)
    except HTTPError, e:
        return 'HTTP Error from urban dictionary Endpoint: %s' % e.message
    except URLError, e:
        return 'Unable to connect to urban dictionary endpoint: %s' % e.message
    else:
        definitions = ''
        support_json = json.loads(response.read())

        if 'list' not in support_json:
            return 'Urban dictionary did not return a result for: %s' % user_input[2]

        for definition in support_json['list']:
            if 'definition' not in definition:
                continue

            definitions += '* %s (%s)\n' % (
                definition['definition'], definition['example'])

        if len(definitions) < 1:
            definitions = '* None\n'

        return 'Definitions matching %s:\n\n%s' % (user_input[2], definitions)
