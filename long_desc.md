# about
- cli scraping application for [nitter](https://nitter.net/search) a popular *twitter mirror    
- works for debain/ubuntu/wsl2 and python3    

## recommended installation
```bash
pip install nitter-miner

# now you can use the nitter cli app 
# default installed to ~/.local/bin/nitter
nitter -q <query> or <query_file> 
```
## manual installation
```bash
# clone and cd to the nitter_stuff repository
git clone 'https://github.com/hashirkz/nitter_scraper'
cd nitter_scraper

python3 -m venv .venv
. ./.venv/bin/activate
python3 -m pip install -r 'requirements.txt'

# for td bank tweets queries defaults to 50pgs
python3 -m __nitter__.nitter_scraper

# for cli application
python3 -m __nitter__.nitter
```  

#### cli usage  
```
nitter -q <query: str> xor -qf <query_file: str> OPTIONS

   -q:   string query to search nitter for *for query formats see /query_info.txt
   
   -qf: 
         if ur constantly searching the same set of queries make a queryfile.csv
         *note the header/first line is ignored.
         ex format of queryfile:
         nasa,spacex,...
         nasa,spacex,...
         @NASA,@SpaceX,

         the actual query which will be searched is 'nasa OR spacex OR @NASA OR @SpaceX'

   *note do not use -q and -qf flags together it will not work also theres no reason to do this

OPTIONS ? DEFAULT:
   -p / --pgs: int, max number of pgs to search for query         ? 50
   -m / --mirror: str -> which mirror to search                   ? https://nitter.net/search
   --retweets: flag -> if present wont filter out retweets        ? false
   --no-sentiments: flag -> if present wont append sentiments     ? false
   --no-save: flag -> if present wont save to a file              ? false
```

#### example usage *see "/tweets/231120_mcgill or mcgill university_262.csv":  
```
>> nitter -q '"mcgill" OR "mcgill university"' -p 50

[nltk_data] Downloading package stopwords to
[nltk_data]     /home/sleepyzzz/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
[nltk_data] Downloading package punkt to /home/sleepyzzz/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package wordnet to
[nltk_data]     /home/sleepyzzz/nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
pgs 1/50
searching https://nitter.net/search?f=tweets&q="mcgill" OR "mcgill university"&since=&until=&near=

pgs 2/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9abby9rQJAAIAAIAAAACCAADAAAAAAgABAAAAAAKAAUX9agjk8AnEAoABhf1qCOTv9jwAAA

pgs 3/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9aVlDpsgwgAIAAIAAAACCAADAAAAAAgABAAAAAEKAAUX9agjk8AnEAoABhf1qCOTv7HgAAA

... **skipping for readme.md but it would go through pgs 4-46 aswell**

pgs 47/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XJLTpaRRgAIAAIAAAACCAADAAAAAAgABAAAAC0KAAUX9agjk8AnEAoABhf1qCOTuPsgAAA

pgs 48/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XFuEpcAQwAIAAIAAAACCAADAAAAAAgABAAAAC4KAAUX9agjk8AnEAoABhf1qCOTuNQQAAA

ity%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XCDc9eRFgAIAAIAAAACCAADAAAAAAgABAAAAC8KAAUX9agjk8AnEAoABhf1qCOTuK0AAAA       

pgs 50/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9W-MNVawWQAIAAIAAAACCAADAAAAAAgABAAAADAKAAUX9agjk8AnEAoABhf1qCOTuIXwAAA

results: 262
```

##### notes
1. OSError: Could not find a suitable TLS CA certificate bundle, invalid path: /etc/ssl/certs/ca-certificates.crt
   1. sudo ln /etc/ssl/certs/<any .pem cert> /etc/ssl/certs/ca-certificates.crt
   2. sudo update-ca-certificates
   
2. issues with emoji package
   1. downgrade to emoji==1.7.0 i.e pip uninstall emoji pip install emoji==1.7.0
   2. uninstall numpy and install numpy == 1.23.0