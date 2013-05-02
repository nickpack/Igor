Set up - OSX
================================
1. Clone the skypekit repository into /usr/local
    git clone git@git.assembla.com:00xx105-cohaesusism.skypekit.git /usr/local/skypekit
2. Clone Igor to wherever you would like it
    git clone git@git.assembla.com:00xx105-cohaesusism.igor.git
3. Install dependencies to allow you to build the Igor virtual environment
    sudo easy_install pip
    sudo pip install virtualenv
4. Change into the root of your Igor clone
5. Set up the virtual environment
    virtualenv venv --no-site-packages --distribute
    source venv/bin/activate
    pip install -r requirements.txt