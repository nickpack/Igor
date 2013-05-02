# -*- coding: utf-8 -*-
import inspect
import string
import settings


def process_command(user_input, **kwargs):

    respond = False

    for name in settings.ADMINS:
        if string.find(kwargs['message'].author.lower(), name) is 0:
            respond = True

    if not respond:
        return 'This is a task to aid development, Please speak to an administrator to perform this action: %s' % settings.ADMINS.join('')
    else:
        if 'conversation' not in kwargs:
            return 'No conversation object provided.'
        if 'message' in kwargs and len(user_input) >= 3 and user_input[2] == 'message':
            for property, value in inspect.getmembers(kwargs['message']):
                kwargs['conversation'].PostText(
                    '* %s: %s\n' % (property, value))
        elif len(user_input) >= 3 and user_input[2] == 'conversationlist':
            if 'skype' not in kwargs:
                return 'Skype object not available'
            else:
                for property, value in inspect.getmembers(kwargs['skype'].GetConversationList('INBOX_CONVERSATIONS')):
                    kwargs['conversation'].PostText(
                        '* %s: %s\n' % (property, value))
        else:
            for property, value in inspect.getmembers(kwargs['conversation']):
                kwargs['conversation'].PostText(
                    '* %s: %s\n' % (property, value))