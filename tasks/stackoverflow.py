# -*- coding: utf-8 -*-
import json
from urllib import quote_plus
from urllib2 import Request, urlopen, HTTPError, URLError
import zlib

# @todo switch to new API
API_URL = 'http://api.stackoverflow.com/1.1/search'


def process_command(user_input, **kwargs):
    if len(user_input) < 3:
        return 'Usage: Igor stackoverflow <topic>'

    topic = quote_plus(user_input[2])

    req = Request('%s/?intitle=%s&page=1&pagesize=5' % (API_URL, topic))

    try:
        response = urlopen(req)
    except HTTPError, e:
        return 'HTTP Error from StackOverflow Endpoint: %s' % e.message
    except URLError, e:
        return 'Unable to connect to StackOverflow endpoint: %s' % e.message
    else:
        gzip_response = zlib.decompress(response.read(), 16 + zlib.MAX_WBITS)

        threads = ''
        threads_json = json.loads(gzip_response)

        if 'total' not in threads_json or threads_json['total'] == 0:
            return 'Stackoverflow returned no results for: %s' % user_input[2]

        for question in threads_json['questions']:
            threads += '* %s: http://stackoverflow.com/%s\n' % (
                question['title'], question['question_timeline_url'])

        if len(threads) < 1:
            threads = '* None\n'

        return 'Top 5 StackOverflow threads for %s:\n\n%s' % (user_input[2], threads)