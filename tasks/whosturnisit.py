from random import choice
from settings import STAFF_NAMES_FOR_BEER


def process_command(user_input, **kwargs):

    responsible_person = choice(STAFF_NAMES_FOR_BEER)
    return 'It is %s\'s turn to put the kettle on.' % responsible_person
