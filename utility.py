import re, htmlentitydefs
from igorexceptions import NoSkypeConversationException, NoSkypeFriendException


def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is

    return re.sub("&#?\w+;", fixup, text)


def get_conversations(skype_instance):
    return skype_instance.GetConversationList('INBOX_CONVERSATIONS')


def get_conversation(conversation_name, skype_instance):
    for convo in get_conversations(skype_instance):
        if convo.displayname.lower().startswith(conversation_name.lower()):
            return convo

    raise NoSkypeConversationException('No conversation found')


def get_friends(skype_instance):
    return skype_instance.GetHardwiredContactGroup('SKYPE_BUDDIES')


def get_friend(skype_instance, friend_name):
    for friend in get_friends(skype_instance):
        if friend.displayname.lower() == friend_name.lower():
            return friend

    raise NoSkypeFriendException('Unable to find a friend called %s' % friend_name)


def get_conversation_with_friend(skype_instance, friend_name):
    friend = get_friend(skype_instance, friend_name)
    return friend.OpenConversation()
