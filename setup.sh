#!/bin/bash

echo "use .venv? recommended yes default no?"
read yn

if [[ "$yn" != "yes" || "$yn" != "y" ]]; then
    pip install -r 'requirements.txt'
    python3 -u nltk_init.py
    
    echo "installed dependencies globally may have compatability issues\nUSAGE: python3 -u app\n"
    exit 0
fi

# creating the .venv 
if [[ ! -d "nitter_stuff" ]]; then
    python3 -m venv nitter_stuff
fi

# installs dependencies to the venv
. ./nitter_stuff/bin/activate
python3 -m pip install -r 'requirements.txt'
python3 -m nltk_init

echo "installed dependencies to ./nitter_stuff venv\nUSAGE . ./nitter_stuff; python3 -m app\n"
exit 0