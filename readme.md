# scraper for [nitter](https://nitter.net/search) *twitter mirror

## usage
this scraper is designed to work in debain/ubuntu/wsl2 
```bash
# clone and cd to the nitter_stuff repository
git clone 'https://github.com/hashirkz/nitter_scraper'
cd nitter_scraper

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
   1. sudo ln /etc/ssl/certs/<any .pem cert> /etc/ssl/certs/ca-certificats.crt
   2. sudo update-ca-certificates
   
2. issues with emoji package
   1. downgrade to emoji==1.7.0 i.e pip uninstall emoji pip install emoji==1.7.0