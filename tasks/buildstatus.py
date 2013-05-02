# -*- coding: utf-8 -*-
import base64
import json
from urllib2 import Request, urlopen, HTTPError, URLError

JENKINS_URL = 'http://jenkins.yourdomain.com/api/json'
JENKINS_USERNAME = 'your.user'
JENKINS_API_KEY = 'your.apikey'
JENKINS_STATUS = {
    'blue': 'Stable',
    'blue_anime': 'Build Running (Stable)',
    'yellow': 'Unstable',
    'yellow_anime': 'Build Running (Last Build Unstable)',
    'red': '**FAILED**',
    'red_anime': 'Build Running (Last Build FAILED)',
    'disabled': '**JOB DISABLED**'
}
EXCLUDE_JOBS = ['Python-Template', 'PHP-Template', 'drupal-template']


def process_command(user_input, **kwargs):
    req = Request(JENKINS_URL)
    base64string = base64.encodestring(
        '%s:%s' % (JENKINS_USERNAME, JENKINS_API_KEY)).replace('\n', '')
    req.add_header("Authorization", "Basic %s" % base64string)
    try:
        response = urlopen(req)
    except HTTPError, e:
        return 'HTTP Error from Jenkins Endpoint: %s' % e.message
    except URLError, e:
        return 'Unable to connect to Jenkins endpoint: %s' % e.message
    else:
        mm_builds = 'Build status:\n\n'
        build_json = json.loads(response.read())

        for job in build_json['jobs']:

            if job['name'] in EXCLUDE_JOBS:
                continue

            colour = job['color']

            if job['color'] in JENKINS_STATUS:
                colour = JENKINS_STATUS[job['color']]

            mm_builds += '* %s: %s\n' % (job['name'], colour)

        return mm_builds
