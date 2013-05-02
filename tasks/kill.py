# -*- coding: utf-8 -*-
from random import choice

WEAPONS = [
    'pair of chinos',
    'bacon sandwich',
    'knife',
    'cucumber',
    'rusty butterknife',
    'fire',
    'wrecking ball',
    'chicken drumstick',
    'baseball bat',
    'house brick',
    'yellow plastic phone',
    'shotgun',
    'massive turd',
    'sandwich',
    'cat',
    'hammer',
    'fixie',
    'wire',
    'keyboard',
    'magic trackpad',
    'phone',
    'bogey',
    'rocket launcher',
    'Graeme',
    'kilt',
    'bagpipe',
    'deep fried pizza',
    'battered mars bar',
    'pixelated glasses',
    'sloppy trout',
    '<head>',
    'skidmark',
    'fixie',
    'synth',
    'spare ticket to my bands gig',
    'dose of new age fun',
    'roll up',
    'pair of tramps underpants',
    'jazz mag',
    'brown paper bag',
    'checked shirt'
]


def process_command(user_input, **kwargs):
    try:
        return '/me kills %s with a %s.' % (user_input[2], choice(WEAPONS))
    except Exception:
        return 'You need to tell me who to murder sire.'
        