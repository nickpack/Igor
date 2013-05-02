# -*- coding: utf-8 -*-
def process_command(user_input, **kwargs):
    try:
        if len(user_input) > 3:
            message = 'Message from %s in %s:\n %s' % (kwargs['author'], kwargs['conversation'].displayname, user_input[3])
        else:
            return 'Usage: Igor sendtogroup <group name|project code> <message>'

        if 'skype' in kwargs:
            for conversation in kwargs['skype'].GetConversationList('INBOX_CONVERSATIONS'):
                if conversation.displayname.lower().startswith(user_input[2].lower()):
                    conversation.PostText(message)
                    return 'Message sent to %s, master.' % user_input[2]
    except Exception, e:
        return 'Please forgive my insolence. %s' % e.message
