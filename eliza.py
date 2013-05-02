# -*- coding: utf-8 -*-
import json
from time import sleep
from datetime import datetime
from urllib2 import Request, urlopen, HTTPError, URLError
from settings import NAG_MESSAGES, ENDPOINTS


processed_messages = []
last_nag = datetime.now()


def run_eliza(conversation_list, stop_event):
    # Some women never stop nagging
    while not stop_event.is_set():
        time_delta = datetime.now() - last_nag
        if time_delta.seconds >= 60:
            check_nags(conversation_list)

        sleep(15)
        check_for_message(conversation_list)
        sleep(15)


def check_nags(conversation_list):
    global last_nag
    current_ts = datetime.now()
    if len(NAG_MESSAGES[current_ts.strftime("%A")]) > 0:
        for nag in NAG_MESSAGES[current_ts.strftime("%A")]:
            if current_ts.hour is nag['hour'] and current_ts.minute is nag['minute']:
                for conversation in conversation_list:
                    if conversation.displayname == 'Cohaesus':
                        conversation.PostText(
                            nag['message']
                        )
                        print 'Eliza: Sent nag message: %s' % nag['message']
                last_nag = datetime.now()


def check_for_message(conversation_list):
    req = Request(ENDPOINTS['messages'])
    req.add_header('Content-Type', 'application/json')
    try:
        response = urlopen(req)
    except HTTPError, e:
        if e.code == 404:
            # No messages in this instance
            pass
        else:
            print 'Eliza: HTTP Error from skybird Endpoint: %s' % e
    except URLError, e:
        print 'Eliza: Unable to connect to skybird endpoint: %s' % e.message
    else:
        try:
            api_json = json.loads(response.read())

            if 'sent' and 'author' and 'message' and 'group' and 'sent' in api_json:
                if api_json['sent'] not in processed_messages:
                    seconds = (api_json['sent'] / 1000) + (api_json['sent'] % 1000.0) / 1000.0
                    datestamp = datetime.datetime.fromtimestamp(seconds)
                    print 'Eliza: Sending message from %s to %s' % (api_json['author'], api_json['group'])
                    for conversation in conversation_list:
                        if conversation.displayname.lower().startswith(api_json['group'].lower()):
                            conversation.PostText(
                                'At %s, %s Said:\n\n' \
                                '%s' % (datestamp, api_json['author'], api_json['message'])
                            )
                            processed_messages.append(api_json['sent'])
                else:
                    print 'Eliza: No new messages...'

                print 'Eliza: %s Total messages sent' % len(processed_messages)

        except Exception:
            # Dont die on exceptions, we'll just try again in the next iteration
            pass