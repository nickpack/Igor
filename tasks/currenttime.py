# -*- coding: utf-8 -*-
from datetime import datetime
from pytz import timezone


def process_command(user_input, **kwargs):
    try:
        if len(user_input) < 3:
            return 'Usage: Igor currenttime <Timezone>'


        tz = timezone(user_input[2])

        fmt = '%d-%m-%Y %H:%M:%S %Z%z'
        loc_dt = timezone('Europe/London').localize(datetime.now())
        time_diff = loc_dt.astimezone(tz)
        return time_diff.strftime(fmt)
    except Exception, e:
        return 'Please forgive my insolence. I was unable to find %s' % e.message