import restsettings


class Root(object):
    pass


def success_response(message):
    response = restsettings.SUCCESS_RESPONSE
    response['message'] = message

    return response


def error_response(error_code, message):
    response = restsettings.ERROR_RESPONSE
    response['message'] = message
    response['error_code'] = error_code

    return response