import os
import signal
from flask import Flask, url_for, render_template

from flask import jsonify
import requests
import simplejson
import json

#from buzz import generator
from stockzBin import getStock
import logging

app = Flask(__name__)
app.debug = False

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def info():
    page = '<html><body><h1>'
    page += "Stockz Version 1"
    page += '</h1></body></html>'
    return page

@app.route("/getStockData/<stockSymbol>")
def stock(stockSymbol):
    logging.info("Entering stock()")

    #https://stackoverflow.com/questions/32201678/how-to-get-json-data-from-a-url-using-flask-in-python
    
    return getStock.data(stockSymbol)

    #displayName = data['items'][0]['display_name']# <-- The display name
    #reputation = data['items'][0]['reputation']# <-- The reputation

    logging.info("Exiting stock()")
    #return Jresponse
    #return ""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
