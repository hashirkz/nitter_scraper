# scraper for [nitter *twitter mirror*] (https://nitter.net/search)

## usage
this scraper is designed to work in debain/ubuntu/wsl2 
```bash
# clone the nitter_stuff repository
git clone 'https://github.com/hashirkz/nitter_scraper'

# create venv and install dependencies
python3 -m venv .venv
. ./.venv/bin/activate

# this may take a while ~1hr
python3 -m pip install -r 'requirements.txt'
python3
>> import nltk
>> nltk.download('all')
...
>> quit()

# in if __name__ == '__main__' for ./nitter_scraper.py
# edit banks being search 
# first run may be slow bc bertweet stuff needs to download
python3 -m nitter_scraper

```