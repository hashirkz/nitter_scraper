# about
- cli scraping application for [nitter](https://nitter.net/search) a popular *twitter mirror    
- works for debain/ubuntu/wsl2 and python3 

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

##### maintaining
1. `/__nitter__/query/bank_queries.csv`
   1. contains all the queries for each bank being searched
   2. add any new banks as columns and any new rows to add new queries to existing banks
   <summary>
   see twitter_queries.csv:
   <details>

   | bmo                 | cibc                               | rbc                         | scotiabank      | td                  |
   |---------------------|------------------------------------|-----------------------------|-----------------|---------------------|
   | @BMO                | CIBC                               | RBCNewsroom                 | Scotiabank      | TDbank              |
   | BMO Field           | CIBCInnovation                     | RBC Newsroom                | ScotiabankHelps | TD Bank             |
   | BMOVanMarathon      | BanqueCIBC                         | RBC_Newsroom                | ScotiabankArena | TD_Bank             |
   | BMOmedia            | TorontoRun                         | @RBC                        | ScotiabankCtr   | TDCanada            |
   | BMOHarrisBank       | CIBC_FCIB                          | RBCCanada                   | ScotiabankTT    | TD Canada           |
   | Bank Of Montreal    | CIBCFCIBBS                         | RBC Canada                  | ScotiabankGY    | TDEconomics         |
   | BankOfMontreal      | CIBCFCIBJM                         | RBC_Canada                  | sccniagara      | TD Economics        |
   | BMO Bank            | CIBCCareers                        | RBCGAMAdvisor               | ScotiaEconomics | TDDirectInvest      |
   | BMO_Bank            | CCS_RFTC_OG                        | RBCGAMNews                  | scotiahockey    | TD DirectInvest     |
   | BMO Capital Markets | CIBCMellon                         | RBC4Students                | GillerPrize     | TD_DirectInvest     |
   | BMO_Media           | CIBCFCIBBB                         | RBCCareers                  | RunCRS          | TDCareers           |
   | lifeatbmo           | CIBC_PWM_US                        | RBCInsurance                | scotiacapital   | TD Careers          |
   |                     | RFTCBlueMtn                        | RBC_Trading                 | ScotiabankViews | TD_Careers          |
   |                     | Canadian Imperial Bank of Commerce | RBC_Insurance               | ScotiabankBB    | TD Garden           |
   |                     | CIBC Private Wealth US             | RBC Insurance               | ScotiaColpatria | TD_Garden           |
   |                     | CIBC Mellon                        | rbc bank                    | RunCRSWest      | TDNewsCanada        |
   |                     | CIBC_Mellon                        | royal bank of canada        | ScotiabankPE    | TDNews Canada       |
   |                     | CIBC Bank                          | RBC Wealth                  | ScotiabankFC    | TDNews_Canada       |
   |                     | CIBC_Bank                          | RBC_Wealth                  | ScotiabankBS    | TDBankUS            |
   |                     | CIBCBank                           | RBCWealth                   | ScotiabankMX    | TDBank US           |
   |                     | CIBC Wood Gundy                    | RBC capital markets         | CHINPicnic      | TDBank_US           |
   |                     | CIBC Run for the Cure              | RBC_capital_markets         | ScotiaCaribbean | TDNewsUS            |
   |                     | CIBC Future Heroes                 | RBCcapitalmarkets           | ScotiabankJM    | TDNews US           |
   |                     | CIBC World Markets                 | RBC Global Asset Management |                 | TDBank US           |
   |                     |                                    | RBC GAM                     |                 | TD_Insurance        |
   |                     |                                    | RBC_GAM                     |                 | TDInsurance         |
   |                     |                                    | RBCGAM                      |                 | TD Insurance        |
   |                     |                                    | rbc visa card               |                 | TD_Canada           |
   |                     |                                    | rbc_bank                    |                 | TD Asset Management |
   |                     |                                    | rbcbank                     |                 | TDAM_Canada         |
   |                     |                                    |                             |                 | TD Visa card        |

   </details>
   </summary>

2. updating css selectors for [nitter](https://nitter.net/search)
   1. in `__nitter__ > nitter_scraper.py > nitter_scraper > search()`
   2. pass selectors for tweet_css='tweet-content', showmore_css='show-more', username_css='username', date_css='tweet-date'
   3. only needed if the html/css changes for nitter.net *probably wont for a while

##### notes
1. OSError: Could not find a suitable TLS CA certificate bundle, invalid path: /etc/ssl/certs/ca-certificates.crt
   1. sudo ln /etc/ssl/certs/<any .pem cert> /etc/ssl/certs/ca-certificates.crt
   2. sudo update-ca-certificates
   
2. issues with emoji package
   1. downgrade to emoji==1.7.0 i.e pip uninstall emoji pip install emoji==1.7.0
   2. uninstall numpy and install numpy == 1.23.0

3. does not work with python >3.10 because of numpy 1.23.0 version issues

##### manual installation **NOT RECOMMENDED**
```bash
# clone and cd to the nitter_stuff repository
git clone 'https://github.com/hashirkz/twitter_scraper'
cd twitter_scraper

python3 -m venv .venv
. ./.venv/bin/activate
python3 -m pip install -r 'requirements.txt'

# for td bank tweets queries defaults to 50pgs
python3 -m __nitter__.nitter_scraper

# for cli application
python3 -m __nitter__.nitter
```  