import requests
import pprint
import os
import urllib.parse
from flask import Flask, redirect, session, jsonify, request
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

conn = sqlite3.connect('stocks.db', check_same_thread=False)
cur = conn.cursor()

sess = {}
api_key = "pk_f99acd61740946c9b13696784a19452e"


@app.route('/')
def hello():
	return "<h1>Welcome to QMUL Stocks Trading!</h1>", 200


@app.route('/stocks/<symbol>', methods=['GET']) 
def get_records(symbol): 
	url = f"https://cloud-sse.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
	response = requests.get(url)
	response.raise_for_status()
	quote = response.json()
	return {
	"name": quote["companyName"],
    "price": float(quote["latestPrice"]),
    "symbol": quote["symbol"]
    }, 200


@app.route('/register', methods = ['POST'])
def register():
	new_user = {'name': request.json['name'], 'pswd': generate_password_hash(request.json['pswd'])}
	#db.update({new_user['name']: new_user['pswd']})
	cur.execute('''INSERT INTO users (username, hash) VALUES (?, ?)''', (new_user['name'], new_user['pswd']))
	conn.commit()
	return jsonify({'message': 'Account registered: {}'.format(request.json['name'])}), 200
	

@app.route("/login", methods=["POST"])
def login():
	#session.clear()
	user = {'name': request.json['name'], 'pswd': request.json['pswd']}
	
	cur.execute('''SELECT * FROM users WHERE username = ?''', (user['name'], ))
	#conn.commit()
	row = cur.fetchall()
	#print(row[0][2])
	if len(row) == 0:
		return jsonify("Kindly register first! {}".format(user['name'])), 401

	if check_password_hash(row[0][2], user['pswd']):
		sess['name'] = user['name']
		return jsonify("Welcome {}!".format(user['name'])), 201
	else:
		return jsonify("Password mismatch {}!".format(user['name'])), 401

@app.route("/reset_password", methods=["PUT"])
def reset_password():
	user = {'name': request.json['name'], 'pswd': request.json['pswd'], 'new_pswd': generate_password_hash(request.json['new_pswd'])}
	cur.execute('''SELECT * FROM users WHERE username = ?''', (user['name'], ))
	row = cur.fetchall()
	if check_password_hash(row[0][2], user['pswd']):
		cur.execute('''UPDATE users SET hash =?''', (user['new_pswd'], ))
		return jsonify("Password changed! ".format(user['name']))
	else:
		return jsonify("Incorrect credentials!"), 401

@app.route("/buy/<symbol>", methods=["POST"])
def buy(symbol):
	url = f"https://cloud-sse.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
	response = requests.get(url)
	response.raise_for_status()
	quote = response.json()
	try:
		cur.execute('''INSERT INTO sales (symbol, price, user_name, share_name) VALUES (?, ?, ?, ?)''', 
	    	(quote["symbol"] , float(quote["latestPrice"]), sess['name'], quote["companyName"]))
		conn.commit()
		#row = cur.execute('''SELECT * FROM sales''')
		#print(row.fetchall()[0])
		return jsonify("Bought! {} at {} for {}".format(quote["companyName"], float(quote["latestPrice"]), sess['name'])), 201
	except KeyError:
		return jsonify("Kindly register or login first!"), 404

@app.route("/records", methods=["GET"])
def display_records():
	try:
		row = cur.execute('''SELECT * FROM sales WHERE user_name = ?''', (sess['name'], ))
		return jsonify(row.fetchall()), 200
	except KeyError:
		return jsonify("Kindly register or login first!"), 404

	#return jsonify(row.fetchall()), 200

@app.route("/return/<r_id>", methods=['DELETE'])
def return_stocks(r_id):
	cur.execute('''DELETE FROM sales WHERE user_name = ? AND id=?''', (sess['name'], r_id))
	conn.commit()
	return jsonify("Success!"), 200

#stocks = {
#"name": quote["companyName"],
#"price": float(quote["latestPrice"]),
#"symbol": quote["symbol"]
#}

if __name__ == '__main__':
	app.run(debug=True)
	print('tearing down')
	conn.close()
