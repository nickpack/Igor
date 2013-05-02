import cherrypy
from igorexceptions import NoSkypeConversationException
from restapi.base import error_response, success_response
from utility import get_conversation


class SendMessageResource():
    skype = None
    exposed = True

    def __init__(self, skype):
        self.skype = skype

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self):
        return self.send_message()

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        return self.send_message()

    def send_message(self):

        inbound_message = cherrypy.request.json

        if 'author' in inbound_message and 'message' in inbound_message and 'to' in inbound_message:
            try:
                convo = get_conversation(inbound_message['to'], self.skype)
                convo.PostText(inbound_message['message'])

                return success_response('Message sent')
            except NoSkypeConversationException:
                return error_response('MSG002', 'Unable to find a conversation with that name.')
            except Exception:
                return error_response('MSG000', 'Unknown Skype Error.')
        else:
            return error_response('MSG001', 'Invalid message payload.')
