# -*- coding: utf-8 -*-
from urllib2 import Request, urlopen, HTTPError, URLError
import xml.etree.ElementTree as ET

TFL_TUBE_API_URL = 'http://cloud.tfl.gov.uk/TrackerNet/LineStatus'


def process_command(user_input, **kwargs):
    req = Request(TFL_TUBE_API_URL)

    try:
        response = urlopen(req)
    except HTTPError, e:
        return 'HTTP Error from TFL Endpoint: %s' % e.message
    except URLError, e:
        return 'Unable to connect to TFL endpoint: %s' % e.message
    else:
        return parse_org_xml(response.read())


def parse_org_xml(xml):
    root = ET.fromstring(xml)

    tube_state = 'Current TFL line status:\n'

    for child in root.findall('{http://webservices.lul.co.uk/}LineStatus'):
        line = child.find('{http://webservices.lul.co.uk/}Line')
        status = child.find('{http://webservices.lul.co.uk/}Status')
        tube_state += '* %s: %s\n' % (
            line.attrib['Name'], status.attrib['Description'])

    return tube_state