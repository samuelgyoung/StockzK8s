from __future__ import print_function
import random

import sys
import os
import signal
from flask import Flask, url_for, render_template

from flask import jsonify
import requests
import simplejson
import json

def data(stockSymbol):
    uri = "https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&fields=symbol,marketState,regularMarketPrice,regularMarketChange,regularMarketChangePercent,preMarketPrice,preMarketChange,preMarketChangePercent,postMarketPrice,postMarketChange,postMarketChangePercent&symbols=" + stockSymbol
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

    return Jresponse

if __name__ == "__main__":
#    print(generate_buzz())
    print ("Entering Main Function")
    #print (sys.argv[1])
    print ("Exiting Main Function")
