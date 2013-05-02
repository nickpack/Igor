# -*- coding: utf-8 -*-

import json
from urllib import quote_plus
from urllib2 import Request, urlopen, HTTPError, URLError

API_URL = 'http://api.factolex.com/v1/search'


def process_command(user_input, **kwargs):
    if len(user_input) < 3:
        return 'Usage: Igor define <topic>'

    topic = quote_plus(user_input[2])

    req = Request('%s/?lang=en&query=%s&format=json' % (API_URL, topic))

    try:
        response = urlopen(req)
    except HTTPError, e:
        return 'HTTP Error from Factolex Endpoint: %s' % e.message
    except URLError, e:
        return 'Unable to connect to Factolex endpoint: %s' % e.message
    else:
        support_json = json.loads(response.read())
        facts = ''
        if 'result' not in support_json:
            return 'No facts found for: %s' % user_input[2]

        for result in support_json['result']:
            for fact in result['facts']:
                facts += '* %s - %s (%s)\n' % (
                    result['title'], fact['title'], fact['source'])

        if len(facts) < 1:
            facts = '* None\n'

        return 'Facts matching %s:\n\n%s' % (user_input[2], facts)