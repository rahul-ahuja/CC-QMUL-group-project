'''
#No longer used due to API issues

import requests
import pprint
import os
import urllib.parse
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
	return "<h1>Welcome to Cloud Merchandise!</h1>"
#check out https://developer.bestbuy.com/

@app.route('/records/<product>', methods=['GET']) 
def get_records(product): 
	API = ##placeholder for API key
	url = f"https://api.bestbuy.com/v1/products(search={urllib.parse.quote_plus(product)})?format=json&show=name,salePrice,sku&apiKey={urllib.parse.quote_plus(API)}"
	response = requests.get(url)
	info = response.json()
	
	return jsonify(info['products'])

if __name__ == '__main__':
	app.run(debug=False)

'''
