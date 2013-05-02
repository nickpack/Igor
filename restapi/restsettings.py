import cherrypy


ERROR_RESPONSE = {
    'error_code': '',
    'message': ''
}

SUCCESS_RESPONSE = {
    'success': True,
    'message': ''
}

CHERRYPY_CONFIG = {
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
    },
}