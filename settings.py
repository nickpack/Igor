import os
from random import choice
import platform

SKYPE_ACCOUNT_NAME = 'botaccount'
SKYPE_ACCOUNT_PASSWORD = 'botaccountpassword'

SKYPE_KIT_PATH = '/usr/local/skypekit' if platform.system().lower() != 'windows' else 'C:/local/skypekit'

RESPOND_TO = ['igor', 'egor', 'slave']

if os.environ.get('DEVELOPMENT', None):
    SKYPE_ACCOUNT_NAME = 'developmentbotaccount'
    SKYPE_ACCOUNT_PASSWORD = 'developmentbotpassword'
    RESPOND_TO = ['devbot']

ENABLE_REST_API = True

SKYPE_KEY_FILE = 'Igor.pem'

LET_IGOR_SPEAK = True

IS_ATTACHED_TO_SONOS = False
SONOS_IP = '10.0.0.62'

ENABLE_ELIZA = True

NAMES_TO_IGNORE = [
    'somenastydude'
]

ADMINS = [
    'nickp666',
]

STAFF_NAMES_FOR_BEER = [
    'Graeme',
    'James',
    'Matt',
    'Richard',
    'Quentin',
    'Dan',
    'Mark',
    'Dave',
    'Ben',
    'Lucy',
    'Shani',
    'Nick Y',
    #'Nick P' # My right as the developer!
]

NAG_MESSAGES = {
    'Monday': [
        {
            'hour': 9,
            'minute': 0,
            'message': 'Good morning everyone, I hope you had a pleasant weekend.'
        }
    ],
    'Tuesday': [
        {
            'hour': 9,
            'minute': 15,
            'message': 'Good morning everybody.'
        }
    ],
    'Wednesday': [
        {
            'hour': 9,
            'minute': 15,
            'message': 'Good morning everybody, I hope the journey to the office wasn\'t too unpleasant.'
        },
        {
            'hour': 14,
            'minute': 30,
            'message': 'Are everyones progress docs up to date?'
        }
    ],
    'Thursday': [
        {
            'hour': 9,
            'minute': 15,
            'message': 'Good morning everyone.'
        }
    ],
    'Friday': [
        {
            'hour': 14,
            'minute': 30,
            'message': 'Can everybody make sure that their status reports are completed today please.'
        },

        {
            'hour': 17,
            'minute': 30,
            'message': 'WOOHOO Its friday! Todays beers are on %s.' % choice(STAFF_NAMES_FOR_BEER)
        }
    ],
    'Saturday': [],
    'Sunday': []
}

ENDPOINTS = {
    'messages': 'http://your.api.com/api/v1/igor/messages'
}

BEHAVIORS = {
    'thanks': 'You are very welcome Master.',
    'dance': '(dance)',
    'you fail': ':( I am sorry Master.',
    'fu': 'I don\'t like your tone Master.',
    'high five': '/me *High Five*'
}
