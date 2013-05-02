#!/bin/bash
cd /home/igor/bot
source venv/bin/activate
git pull origin develop
pip install -r requirements.txt
sudo service igor restart
