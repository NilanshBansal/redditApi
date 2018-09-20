from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import json
import argparse
import csv
import urllib

app = Flask(__name__)

@app.route('/')
def home():
    searchQuery = request.args.get('q')
    if searchQuery is None:
        searchQuery = 'ico scam'
    subreddit = request.args.get('s')
    if subreddit is None:
        subreddit = 'ethtrader'
    limit = request.args.get('l')
    if limit is None:
        limit = 25
    url = 'https://api.pushshift.io/reddit/search/submission/?q=' + urllib.parse.quote_plus(searchQuery) + '&subreddit=' + urllib.parse.quote_plus(
        subreddit) + '&size=' + str(limit) + '&filter=author,created_utc,full_link,id,num_comments,retrieved_on,score,selftext,title,url'

    response = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

    data = response.text

    return data


app.run(port=5000)
