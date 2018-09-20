import requests
from bs4 import BeautifulSoup
import json
import argparse
import csv
import urllib

# For use with Tor
proxies = {
    # 'http': 'socks5h://127.0.0.1:9050',
    # 'https': 'socks5h://127.0.0.1:9050'
}

parser = argparse.ArgumentParser(
    usage='reddit.py [-h] [-l] <limitResults> [-s] <Subreddit> [-q] <SearchQuery>')


optional = parser._action_groups.pop()
# required = parser.add_argument_group('required arguments')

optional.add_argument('-l', type=int, help='No of comment threads')
optional.add_argument('-s', type=str, help='Subreddit to search in')
optional.add_argument('-q', type=str, help='Search Keyword')
parser._action_groups.append(optional)


if parser.parse_args().q == None:
    searchQuery = 'ico scam'
else:
    searchQuery = parser.parse_args().q

if parser.parse_args().s == None:
    subreddit = 'ethtrader'
else:
    subreddit = parser.parse_args().s

if parser.parse_args().l == None:
    limit = 25
else:
    limit = parser.parse_args().l


url = 'https://api.pushshift.io/reddit/search/submission/?q=' + urllib.parse.quote_plus(searchQuery) + '&subreddit=' + subreddit + '&size=' + str(
    limit) + '&filter=author,created_utc,full_link,id,num_comments,retrieved_on,score,selftext,title,url'
data = requests.get(url, proxies=proxies, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).text

# print(json.loads(data))
json_data = json.loads(data)

fieldNames = ['id', 'author', 'title', 'full_link', 'selftext',
              'created_utc', 'num_comments', 'retrieved_on', 'score', 'url']

filename = searchQuery + '_' + subreddit + '.csv'

with open(filename, 'w') as f:
    writer = csv.DictWriter(f, fieldNames)
    writer.writeheader()
    for thread in json_data['data']:
        writer.writerow(thread)
