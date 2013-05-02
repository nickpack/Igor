# -*- coding: utf-8 -*-
import signal
import sys
import threading
import traceback
from time import sleep
import time
import cherrypy
from eliza import run_eliza
import re
from restapi.base import Root
from restapi.resources.messages import SendMessageResource
from restapi.restsettings import CHERRYPY_CONFIG
import settings
from unicodeshlex import unicodeshlex as shlex
import utility
from BeautifulSoup import BeautifulSoup
from pymongo import Connection as MongoConnection
from threading import Thread

sys.path.append(settings.SKYPE_KIT_PATH + '/ipc/python')
sys.path.append(settings.SKYPE_KIT_PATH + '/interfaces/skype/python')

account_name = settings.SKYPE_ACCOUNT_NAME
account_pass = settings.SKYPE_ACCOUNT_PASSWORD
logged_in = False
eliza_stop_event = threading.Event()


def signal_handler(signum, frame):
    # A little bit pokemon, but SIGINT and SIGTERM handling in this case yields the same result
    # and I havent implemented any of the other signals as yet
    if settings.ENABLE_ELIZA:
        print('Telling Eliza to stop...')
        eliza_stop_event.set()

    igor_skype.stop()

    sys.exit()


# self in non-class scope? really skype?
def on_message(self, incoming_message, changesInboxTimestamp, supersedesHistoryMessage, conversation):

    mentioned = False
    respond = False

    if incoming_message.author != account_name:
        message = utility.unescape(''.join(
            BeautifulSoup(incoming_message.body_xml).findAll(
                text=True,
                convertEntities='html'
            )
        ))

        for name in settings.RESPOND_TO:
            if name in message.lower():
                mentioned = True
                respond = message.lower().startswith(name)
                break

        if mentioned and not respond:
            for name, response in settings.BEHAVIORS.iteritems():
                if message.lower().startswith(name):
                    conversation.PostText(response)

        if respond:

            if incoming_message.author.lower() in settings.NAMES_TO_IGNORE:
                conversation.PostText('I\'m not at leisure to answer your question.')
                return

            # @todo Usage log
            #print u'Igor: %s issued command: %s' % (incoming_message.author_displayname, message.encode('utf-8'))

            command_parts = [i.encode('utf-8') for i in shlex.split(message)]

            if len(command_parts) < 2:
                conversation.PostText('Yes, Master?')
            else:
                t = Thread(target=execute_task, args=(command_parts, incoming_message, conversation))
                t.start()


def account_on_change(self, property_name):
    global logged_in
    if property_name == 'status':
        if self.status == 'LOGGED_IN':
            logged_in = True
            print('Logged in to Skype...')


def main():
    global igor_skype
    global mongo_connection

    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    try:
        import Skype
    except ImportError:
        raise SystemExit('Program requires Skype and skypekit modules.')

    try:
        mongo_connection = MongoConnection()
    except Exception:
        print 'Unable to connect to MongoDB - Did you remember to start it?'
        mongo_connection = False

    try:
        print 'Attempting to log in to Skype...'
        igor_skype = Skype.GetSkype(settings.SKYPE_KEY_FILE)
        igor_skype.Start()
        account = igor_skype.GetAccount(account_name)
        account.LoginWithPassword(account_pass, False, False)
    except Exception, e:
        raise SystemExit('Unable to create skype instance: %s' % e.message)

    Skype.Account.OnPropertyChange = account_on_change
    Skype.Skype.OnMessage = on_message

    while not logged_in:
        sleep(1)

    if settings.ENABLE_ELIZA:
        # Give skypekit some time to populate the conversation list.
        print('Waking up Eliza and giving her 15 seconds to get herself together...')
        time.sleep(15)
        eliza_thread = Thread(target=run_eliza, args=(igor_skype.GetConversationList('INBOX_CONVERSATIONS'), eliza_stop_event))
        eliza_thread.start()

    print('At your service, master...')

    if settings.ENABLE_REST_API:
        print ('Enabling REST API...')

        root = Root()
        root.sendmessage = SendMessageResource(igor_skype)
        cherrypy.config.update('restapi.conf')
        cherrypy.config.update(CHERRYPY_CONFIG)

        app = cherrypy.tree.mount(root, '/', 'restapi.conf')
        app.merge(CHERRYPY_CONFIG)

        cherrypy.engine.start()
        cherrypy.engine.block()


def execute_task(command_parts, incoming_message, conversation):

    message_author = incoming_message.author_displayname.split(' ', 1)
    action = re.sub('[\W_]+', '', command_parts[1].lower())
    try:
        command_module = __import__("tasks.%s" % action, fromlist=['process_command'])

        to_say = command_module.process_command(
            command_parts,
            conversation=conversation,
            mongo=mongo_connection,
            author=incoming_message.author_displayname,
            message=incoming_message,
            skype=igor_skype
        )

    except ImportError, e:
        to_say = 'Sorry master %s, I do not know what you mean. %s' % (message_author[0], e.message)
    except AttributeError, e:
        to_say = 'Sorry master %s, it looks like this command is broken. %s' % (e.message, message_author[0])
    except Exception, e:
        traceback.print_exc()
        to_say = 'Forgive my insolence master, but I had difficulty executing your specified command. %s' % e.message

    conversation.PostText(to_say)


if __name__== "__main__":
    main()
