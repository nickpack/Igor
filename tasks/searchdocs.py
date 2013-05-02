# -*- coding: utf-8 -*-
from urllib import quote_plus

DOCUMENTATION_URLS = {
    'python': 'http://docs.python.org/2/search.html?q=%s&check_keywords=yes&area=default',
    'django': 'https://docs.djangoproject.com/search/?q=%s',
    'php': 'http://php.net/%s',
    'java': 'http://search.oracle.com/search/search?search_p_main_operator=all&group=Documentation&q=%s',
    'jquery': 'http://api.jquery.com/?ns0=1&s=%s',
    'googlemaps': 'https://developers.google.com/search/results?q=%s&p=%%2Fmaps%%2Fdocumentation%%2Fjavascript',
    'cakephp': 'http://api21.cakephp.org/search/%s',
    'zendframework': 'https://www.google.com/search?q=%s&sitesearch=framework.zend.com',
    'symfony': 'http://symfony.com/search?q=%s',
    'spring': 'http://www.springsource.org/search/google?query=%s&output=xml_no_dtd&client=google-csbe&cx=009687201310241541466%%3Azerjfa_shxo&ie=utf-8&oe=utf-8&op=Search'
}


def process_command(user_input, **kwargs):
    if len(user_input) < 4:
        return 'Usage: Igor searchdocs <language|project name> <term>'
    else:
        if user_input[2].lower() in DOCUMENTATION_URLS:
            return DOCUMENTATION_URLS[user_input[2].lower()] % (quote_plus(user_input[3]))
        else:
            output = 'Unknown Documentation Source - Available sources:\n'
            for key, value in DOCUMENTATION_URLS.iteritems():
                output += '* %s\n' % key

            return output
