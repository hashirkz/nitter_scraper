# scraper for [nitter](https://nitter.net/search) *twitter mirror

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

### notes
1. OSError: Could not find a suitable TLS CA certificate bundle, invalid path: /etc/ssl/certs/ca-certificates.crt
   1. sudo ln /etc/ssl/certs/<any .pem cert> /etc/ssl/certs/ca-certificats.crt
   2. sudo update-ca-certificates
   
2. issues with emoji package
   1. downgrade to emoji==1.7.0 i.e pip uninstall emoji pip install emoji==1.7.0