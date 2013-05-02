# -*- coding: utf-8 -*-
import json
from urllib import quote_plus
from urllib2 import Request, urlopen, HTTPError, URLError

API_URL = 'http://api.html5please.com'


def process_command(user_input, **kwargs):
    if len(user_input) < 3:
        return 'Usage: Igor caniuse <tags>'

    tags = quote_plus(user_input[2])

    req = Request('%s/%s.json' % (API_URL, tags))
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4')

    try:
        response = urlopen(req)
    except HTTPError, e:
        return 'HTTP Error from html5please Endpoint: %s' % e.message
    except URLError, e:
        return 'Unable to connect to html5please endpoint: %s' % e.message
    else:
        browsers = ''
        support_json = json.loads(response.read())

        if 'results' not in support_json:
            return 'html5please did not return a result for selector/tag: %s' % user_input[2]

        for browser, ver in support_json['results'].iteritems():
            browsers += '* %s: %s\n' % (browser, ver)

        if len(browsers) < 1:
            browsers = '* None\n'

        return '%s is supported in:\n\n%s' % (user_input[2], browsers)
