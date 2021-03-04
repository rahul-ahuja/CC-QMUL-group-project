import requests
import pprint
import os
import urllib.parse
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
	return "<h1>Welcome to Cloud Merchandise!</h1>"


@app.route('/records/<product>', methods=['GET']) 
def get_records(product): 
	API = ##placeholder for API key
	url = f"https://api.bestbuy.com/v1/products(search={urllib.parse.quote_plus(product)})?format=json&show=name,salePrice,sku&apiKey={urllib.parse.quote_plus(API)}"
	response = requests.get(url)
	info = response.json()
	
	return jsonify(info['products'])

if __name__ == '__main__':
	app.run(debug=False)


"""
url = "https://api.bestbuy.com/v1/products(search=oven&search=stainless&search=steel)?format=json&show=name,salePrice&apiKey=1C4dw6IqyHgMzfGExxcIoqxa"
url = "https://api.bestbuy.com/v1/products(search=computer&search=games)?format=json&show=name,salePrice&apiKey=1C4dw6IqyHgMzfGExxcIoqxa"

url = "https://api.bestbuy.com/v1/products(search=computer&search=games)?format=json&show=name,salePrice&apiKey=1C4dw6IqyHgMzfGExxcIoqxa"

url = f"https://cloud-sse.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"



product = "computer"
url = f"https://api.bestbuy.com/v1/products(search={urllib.parse.quote_plus(product)})?format=json&show=name,salePrice,sku&apiKey=1C4dw6IqyHgMzfGExxcIoqxa"

info = requests.get(url)
response = info.json()

pprint.pprint(response['products'])
"""
