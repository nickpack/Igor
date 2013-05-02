# -*- coding: utf-8 -*-
from settings import SONOS_IP, IS_ATTACHED_TO_SONOS
from soco.soco import SoCo


def process_command(user_input, **kwargs):
    if len(user_input) < 3:
        return 'Usage: Igor sonos <play|pause|stop|next|previous|current|partymode|mute|unmute|volume>'

    if not IS_ATTACHED_TO_SONOS:
        return 'Sorry master, I cannot presently communicate with the Sonos.'

    cmd = user_input[2]

    sonos = SoCo(SONOS_IP)

    if cmd == 'partymode':
        action = sonos.partymode()
        if action:
            return 'Party Mode Enabled.'
    elif cmd == 'play':
        action = sonos.play()
        if action:
            return 'You should hear the funky music, Master.'
    elif cmd == 'pause':
        action = sonos.pause()
        if action:
            return 'Music paused, Master.'
    elif cmd == 'stop':
        action = sonos.stop()
        if action:
            return 'I have stopped that vile racket, Master.'
    elif cmd == 'next':
        action = sonos.next()
        if action:
            track = sonos.get_current_track_info()
            return 'Now playing: %s - %s, From Album: %s' % (track['artist'], track['title'], track['album'])
    elif cmd == 'previous':
        action = sonos.previous()
        if action:
            track = sonos.get_current_track_info()
            return 'Now re-playing: %s - %s, From Album: %s' % (track['artist'], track['title'], track['album'])
    elif cmd == 'mute':
        action = sonos.mute(True)
        if action:
            return 'I have silenced that vile racket, Master.'
    elif cmd == 'unmute':
        action = sonos.mute(False)
        if action:
            return 'Play that funky music white boy.'
    elif cmd == 'current':
        track = sonos.get_current_track_info()
        return 'Current track: %s - %s, From Album: %s' % (track['artist'], track['title'], track['album'])
    elif cmd == 'volume':
        if len(user_input) < 4:
            return 'I need to know how loud master.'
        else:
            if int(user_input[3]) <= 100 and int(user_input[3]) > 0:
                action = sonos.volume(int(user_input[3]))
                if action:
                    return 'Volume setting changed master.'
            else:
                return 'Master, I require a volume value of between 1 and 100'
    else:
        return "Valid commands: play, pause, stop, next, previous, current, and partymode"
