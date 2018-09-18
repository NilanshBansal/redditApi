
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

    limit = request.args.get('l')

    if limit is None:
        limit = 25

    url = 'http://elastic.pushshift.io/rs/submissions/_search/?q=(title:' + searchQuery + '%20OR%20selftext:' + searchQuery + 'AND%20score:%3E100)&sort=created_utc:desc&size=' + str(limit) 


    response = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

    data = response.text
    test(json.loads(data))
    return data

#REMOVE DELETED RESULTS
def test(data):
    for thread in data['hits']['hits']:
        print(thread['_source']['permalink'])
        
    pass
    
app.run(port=5000)
