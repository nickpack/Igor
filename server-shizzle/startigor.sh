#!/bin/bash
cd /usr/local/skypekit && python startskypekit.py --skypekit=./bin/linux-x86/linux-x86-skypekit &
cd /home/igor/bot
source venv/bin/activate
python igor.py