# -*- coding: utf-8 -*-
import json
from urllib import quote_plus
from urllib2 import Request, urlopen, HTTPError, URLError

API_URL = 'https://api.github.com/legacy/repos/search'


def process_command(user_input, **kwargs):
    if len(user_input) < 3:
        return 'Usage: Igor github <query> <language>'

    query = quote_plus(user_input[2])
    url = '%s/%s' % (API_URL, query)

    if len(user_input) > 3:
        url += '?language=%s' % quote_plus(user_input[3])

    req = Request(url)

    try:
        response = urlopen(req)
    except HTTPError, e:
        return 'HTTP Error from github Endpoint: %s' % e.message
    except URLError, e:
        return 'Unable to connect to github endpoint: %s' % e.message
    else:
        repos = ''
        support_json = json.loads(response.read())

        if 'repositories' not in support_json:
            return 'Github did not return a result for: %s' % user_input[2]

        for repository in support_json['repositories']:
            description = (repository['description'][:50] + '..') if len(
                repository['description']) > 50 else repository['description']
            repos += '* %s (%s): https://github.com/%s/%s\n' % (repository['name'], description, repository['owner'], repository['name'])

        if len(repos) < 1:
            repos = '* None\n'

        return 'Repositories matching %s:\n\n%s' % (user_input[2], repos)
