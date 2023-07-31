import pandas as pd                 # 2.0.2
import numpy as np                  # 1.24.1         

from bs4 import BeautifulSoup       # 0.0.1
import requests                     # 2.28.1
import tabulate                     # 0.9.0
from langdetect import detect       # 1.0.9

import os
import re
import string
# from functools import map

# SETTINGS AND GLOBAL STUFF

HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    }

class nitter_scraper:
    
    def __init__(self, headers=HEADERS, domain='https://nitter.net/search'):
        self._headers = headers
        self._domain = domain

    def search(self, q: str='', max_pgs: int=10, tweet_css='tweet-content', showmore_css='show-more', clean: bool=True, lang='en', show_rt: bool=False):
        url = nitter_scraper.form_query(q)


        tweets = []
        for pg in range(max_pgs):
            resp = requests.get(url, headers=self._headers)
            soup = BeautifulSoup(resp.text, 'html.parser')

            print(f'pgs {pg+1}/{max_pgs}')
            print(f'searching {url}\n')
            results = list(soup.find_all(class_=tweet_css))
            if results: 
                for tweet in results:
                    # clean tweet
                    tweet = nitter_scraper.reformat_text(tweet.text) if clean else tweet.text

                    # skip if not in desired language 
                    if detect(tweet) != lang: continue

                    # skip if not showing retweets
                    if not show_rt and tweet.lower().startswith('rt'): continue

                    tweets.append(tweet)


            # navigate to next page if it exists 
            # the -1 because the selector will also pick up the previous page link
            show_more = soup.find_all(class_=showmore_css)[-1]
            if not show_more:
                break

            url = show_more.findChild('a')['href']
            url = f'{self._domain}/{url}'

        print(f'results: {len(tweets)}\n')
        return pd.DataFrame(np.array(tweets))


        # for i, tweet in enumerate(search_results):
        #     print(f'tweet_{i}: {nitter_scraper.reformat_text(tweet.text)}\n')

    
    '''
        generates formatted query to search nitter.net
        how to format search queries *q:
        https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query

        exs:
        snow day #noschool                          searches tweets with the words snow and day and hashtag #noschool
        snow OR day OR #noschool                    searches tweets with snow or day or the hashtag #noschool
        (@twitterdev OR @twitterapi) -@twitter      searches tweets that mention (@twitterdev or @twitterapi) and dont mention @twitter

        notes/useful:
        -is:retweet                                 for filtering out retweets *seems not working
        -                                           for negative
        #                                           for hashtags
        @user                                       for tweets mentioning user
        is:                                         for filtering tweets
        has:                                        for filtering e.x has:images
        from:user                                   for filtering tweets from user
        ()                                          for grouping terms
        OR                                          for matching term_i or term_j *default AND when no separator
        "term1 term2..."                            for terms with spaces
    '''
    @staticmethod
    def form_query(q: str, endpoint: str='https://nitter.net/search', since: str='', until: str='', near: str=''):
        f = 'tweets'
        url = f'{endpoint}?f={f}&q={q}&since={since}&until={until}&near={near}'
        return url
    
    # formats text by all alphanumeric lowercase no trailing punctuation + ' ' \n no special characters
    # edit this to apply more filters on resp.full_text
    @staticmethod
    def reformat_text(text: str) -> str:
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        text = text.replace('\n', ' ')
        text = re.sub(r'http.*', '', text)
        text = text.strip(string.punctuation + string.whitespace)
        return text



if __name__ == '__main__':
    nitter = nitter_scraper()
    tweets = nitter.search(q='scotiabank')

    tweets.to_csv('./scotiabank_stuff.csv')
    # text = 'hello there whats up today'
    # print(detect(text))