def process_command(user_input, **kwargs):
    skype_buddies = kwargs['skype'].GetHardwiredContactGroup('SKYPE_BUDDIES')
    skype_contacts = skype_buddies.GetContacts()

    if len(user_input) < 3:
        return 'You need to give me the name Master.'

    convo = None

    for contact in skype_contacts:
        if contact.displayname == kwargs['author']:
            convo = contact.OpenConversation()
            break

    if not convo:
        return 'Unable to open a conversation with %s - Are they on my friends list?' % kwargs['author']

    identities_to_add = ['rbundock']
    new_group = convo.SpawnConference(identities_to_add)
    new_group.SetTopic(user_input[2])
    new_group.PostText('Hello everyone, welcome to %s.' % user_input[2])

    return 'I have created the group master.'