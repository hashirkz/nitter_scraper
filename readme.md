# scraper for [nitter](https://nitter.net/search) *twitter mirror

## usage
this scraper is designed to work in debain/ubuntu/wsl2 
```bash
# clone and cd to the nitter_stuff repository
git clone 'https://github.com/hashirkz/nitter_scraper'
cd nitter_scraper

# AUTOMATED SETUP
./setup.sh
. ./nitter_stuff/bin/activate

# bank tweets searcher already setup not dynamic
python3 -m nitter_scraper

# cli utility see cli usage below
python3 -m nitter
```  
### maintaining
1. `./twitter_queries.csv`
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
   1. in nitter_scraper.py > nitter_scraper > search()
   2. pass selectors for tweet_css='tweet-content', showmore_css='show-more', username_css='username', date_css='tweet-date'
   3. only needed if the html/css changes for nitter.net *probably wont for a while

#### notes
1. OSError: Could not find a suitable TLS CA certificate bundle, invalid path: /etc/ssl/certs/ca-certificates.crt
   1. sudo ln /etc/ssl/certs/<any .pem cert> /etc/ssl/certs/ca-certificates.crt
   2. sudo update-ca-certificates
   
2. issues with emoji package
   1. downgrade to emoji==1.7.0 i.e pip uninstall emoji pip install emoji==1.7.0
   2. 
##### cli usage
python3 -m nitter <query: str> xor <query_file: str> OPTIONS

*xor meaning only 1 of these can be used at a time dont mix together lol
query:         
   query to search nitter for
query_file:    
   if ur constantly searching the same set of queries make a queryfile
   to avoid having to retype commands and stuff e.x ./twitter_queries.csv
   has banks as columns and under each bank the queries to search for

OPTIONS ? DEFAULT:
   -p / --pgs: int, max number of pgs to search for query         ? 50
   -m / --mirror: str -> which mirror to search                   ? https://nitter.net/search
   --retweets: flag -> if present wont filter out retweets        ? false
   --no-sentiments: flag -> if present wont append sentiments     ? false
   --no-save: flag -> if present wont save to a file              ? false


example usage *see "./231120_mcgill or mcgill university_262.csv":  
```
>> python3 -m nitter -q '"mcgill" OR "mcgill university"' -p 50
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

pgs 4/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9aKKVZaAuQAIAAIAAAACCAADAAAAAAgABAAAAAIKAAUX9agjk8AnEAoABhf1qCOTv4rQAAA

pgs 5/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9Z8QwlcAIAAIAAIAAAACCAADAAAAAAgABAAAAAMKAAUX9agjk8AnEAoABhf1qCOTv2PAAAA

pgs 6/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9ZuI9tvQdgAIAAIAAAACCAADAAAAAAgABAAAAAQKAAUX9agjk8AnEAoABhf1qCOTvzywAAA

pgs 7/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9Zj3BJqR7AAIAAIAAAACCAADAAAAAAgABAAAAAUKAAUX9agjk8AnEAoABhf1qCOTvxWgAAA

pgs 8/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9ZY0V1uRvwAIAAIAAAACCAADAAAAAAgABAAAAAYKAAUX9agjk8AnEAoABhf1qCOTvu6QAAA

pgs 9/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9ZQrIBtxKAAIAAIAAAACCAADAAAAAAgABAAAAAcKAAUX9agjk8AnEAoABhf1qCOTvseAAAA

pgs 10/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9ZKAedphugAIAAIAAAACCAADAAAAAAgABAAAAAgKAAUX9agjk8AnEAoABhf1qCOTvqBwAAA

pgs 11/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9ZDxMdqBzgAIAAIAAAACCAADAAAAAAgABAAAAAkKAAUX9agjk8AnEAoABhf1qCOTvnlgAAA

pgs 12/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9Y9Q1Nbh0wAIAAIAAAACCAADAAAAAAgABAAAAAoKAAUX9agjk8AnEAoABhf1qCOTvlJQAAA

pgs 13/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9Y4ropbxDgAIAAIAAAACCAADAAAAAAgABAAAAAsKAAUX9agjk8AnEAoABhf1qCOTvitAAAA

pgs 14/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9Y1EE9rQ5gAIAAIAAAACCAADAAAAAAgABAAAAAwKAAUX9agjk8AnEAoABhf1qCOTvgQwAAA

pgs 15/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9Ywwy5uxGAAIAAIAAAACCAADAAAAAAgABAAAAA0KAAUX9agjk8AnEAoABhf1qCOTvd0gAAA

pgs 16/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9YtLYJqRmAAIAAIAAAACCAADAAAAAAgABAAAAA4KAAUX9agjk8AnEAoABhf1qCOTvbYQAAA

pgs 17/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9YocKFbQ8QAIAAIAAAACCAADAAAAAAgABAAAAA8KAAUX9agjk8AnEAoABhf1qCOTvY8AAAA

pgs 18/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9Ykw8ZYgJwAIAAIAAAACCAADAAAAAAgABAAAABAKAAUX9agjk8AnEAoABhf1qCOTvWfwAAA

pgs 19/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9YhKFVehBgAIAAIAAAACCAADAAAAAAgABAAAABEKAAUX9agjk8AnEAoABhf1qCOTvUDgAAA

pgs 20/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9Ycov5qAOgAIAAIAAAACCAADAAAAAAgABAAAABIKAAUX9agjk8AnEAoABhf1qCOTvRnQAAA

pgs 21/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9YXgWtewFAAIAAIAAAACCAADAAAAAAgABAAAABMKAAUX9agjk8AnEAoABhf1qCOTvPLAAAA

pgs 22/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9YU4H9aQZgAIAAIAAAACCAADAAAAAAgABAAAABQKAAUX9agjk8AnEAoABhf1qCOTvMuwAAA

pgs 23/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9YR-WZZATAAIAAIAAAACCAADAAAAAAgABAAAABUKAAUX9agjk8AnEAoABhf1qCOTvKSgAAA

pgs 24/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9YOa7BqQyQAIAAIAAAACCAADAAAAAAgABAAAABYKAAUX9agjk8AnEAoABhf1qCOTvH2QAAA

pgs 25/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9YKVXlbR1wAIAAIAAAACCAADAAAAAAgABAAAABcKAAUX9agjk8AnEAoABhf1qCOTvFaAAAA

pgs 26/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9YHz0tth6gAIAAIAAAACCAADAAAAAAgABAAAABgKAAUX9agjk8AnEAoABhf1qCOTvC9wAAA

pgs 27/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9YGWc1ugNwAIAAIAAAACCAADAAAAAAgABAAAABkKAAUX9agjk8AnEAoABhf1qCOTvAhgAAA

pgs 28/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9YDvGReBiAAIAAIAAAACCAADAAAAAAgABAAAABoKAAUX9agjk8AnEAoABhf1qCOTu-FQAAA

pgs 29/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9YBlBRbBiwAIAAIAAAACCAADAAAAAAgABAAAABsKAAUX9agjk8AnEAoABhf1qCOTu7pAAAA

pgs 30/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9X_MT5cgXAAIAAIAAAACCAADAAAAAAgABAAAABwKAAUX9agjk8AnEAoABhf1qCOTu5MwAAA

pgs 31/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9X7zHNYRmQAIAAIAAAACCAADAAAAAAgABAAAAB0KAAUX9agjk8AnEAoABhf1qCOTu2wgAAA

pgs 32/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9X4IrNvAfwAIAAIAAAACCAADAAAAAAgABAAAAB4KAAUX9agjk8AnEAoABhf1qCOTu0UQAAA

pgs 33/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9X1xINpQZwAIAAIAAAACCAADAAAAAAgABAAAAB8KAAUX9agjk8AnEAoABhf1qCOTux4AAAA

pgs 34/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XztZtYRMwAIAAIAAAACCAADAAAAAAgABAAAACAKAAUX9agjk8AnEAoABhf1qCOTuvbwAAA

pgs 35/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9Xww5NfBhAAIAAIAAAACCAADAAAAAAgABAAAACEKAAUX9agjk8AnEAoABhf1qCOTus_gAAA

pgs 36/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XupEpfQDAAIAAIAAAACCAADAAAAAAgABAAAACIKAAUX9agjk8AnEAoABhf1qCOTuqjQAAA

pgs 37/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XtAZJbwtwAIAAIAAAACCAADAAAAAAgABAAAACMKAAUX9agjk8AnEAoABhf1qCOTuoHAAAA

pgs 38/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XqEZhrgowAIAAIAAAACCAADAAAAAAgABAAAACQKAAUX9agjk8AnEAoABhf1qCOTulqwAAA

pgs 39/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XnTWRYgFwAIAAIAAAACCAADAAAAAAgABAAAACUKAAUX9agjk8AnEAoABhf1qCOTujOgAAA

pgs 40/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XktFpZgqgAIAAIAAAACCAADAAAAAAgABAAAACYKAAUX9agjk8AnEAoABhf1qCOTugyQAAA

pgs 41/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XhLBZoQFgAIAAIAAAACCAADAAAAAAgABAAAACcKAAUX9agjk8AnEAoABhf1qCOTueWAAAA

pgs 42/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XdZEtfBpAAIAAIAAAACCAADAAAAAAgABAAAACgKAAUX9agjk8AnEAoABhf1qCOTub5wAAA

pgs 43/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XWv4ZtQIQAIAAIAAAACCAADAAAAAAgABAAAACkKAAUX9agjk8AnEAoABhf1qCOTuZdgAAA

pgs 44/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XUMQFdxxgAIAAIAAAACCAADAAAAAAgABAAAACoKAAUX9agjk8AnEAoABhf1qCOTuXBQAAA

pgs 45/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XPdW5dAWAAIAAIAAAACCAADAAAAAAgABAAAACsKAAUX9agjk8AnEAoABhf1qCOTuUlAAAA

pgs 46/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XLXGxsgqAAIAAIAAAACCAADAAAAAAgABAAAACwKAAUX9agjk8AnEAoABhf1qCOTuSIwAAA

pgs 47/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XJLTpaRRgAIAAIAAAACCAADAAAAAAgABAAAAC0KAAUX9agjk8AnEAoABhf1qCOTuPsgAAA

pgs 48/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XFuEpcAQwAIAAIAAAACCAADAAAAAAgABAAAAC4KAAUX9agjk8AnEAoABhf1qCOTuNQQAAA

ity%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9XCDc9eRFgAIAAIAAAACCAADAAAAAAgABAAAAC8KAAUX9agjk8AnEAoABhf1qCOTuK0AAAA       

pgs 50/50
searching https://nitter.net/search/?f=tweets&q=%22mcgill%22+OR+%22mcgill+university%22&cursor=DAADDAABCgABF_Wn_9hW8WQKAAIX9W-MNVawWQAIAAIAAAACCAADAAAAAAgABAAAADAKAAUX9agjk8AnEAoABhf1qCOTuIXwAAA

results: 262
```
