# about
- cli scraping application for [nitter](https://nitter.net/search) a popular *twitter mirror    
- works for debain/ubuntu/wsl2 and python3 
- **01/05/24 - WORKING**  
- 
## installation
```bash
# install nitter cli application
pip install nitter-miner

# if youve never used nltk you have to do this its silly but yea
python3 -c "import nltk; nltk.download('all')"

# now you can use the nitter cli app 
# default installed to ~/.local/bin/nitter
nitter -q <query> or <query_file> 
```

### cli usage  
#nitter-miner: 0.1.0 
`nitter -q <query: str> xor -qf <query_file: str>`

REQUIRED:    
- q:   string query to search nitter for \*for query formats see /query_info.txt  

- qf:  
      if ur constantly searching the same set of queries make a queryfile.csv  
      *note the header/first line is ignored.  
      ex format of queryfile:  
      nasa,spacex,...  
      nasa,spacex,...  
      @NASA,@SpaceX,...  
   the actual query which will be searched is `nasa OR spacex OR @NASA OR @SpaceX`  

\*note do not use -q and -qf flags together it will not work also theres no reason to do this  

```
OPTIONS                                                          ? DEFAULT  
--------------------------------------------------------------------------------------------    
- -p / --pgs: int, max number of pgs to search for query         ? 50  
- -m / --mirror: str -> which mirror to search                   ? https://nitter.net/search  
- --retweets: flag -> if present wont filter out retweets        ? false   
- --no-sentiments: flag -> if present wont append sentiments     ? false   
- --no-save: flag -> if present wont save to a file              ? false   
```

#### example usage see `/tweets/231120_mcgill or mcgill university_262.csv`: 
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