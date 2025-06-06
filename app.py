#importing libraries
import requests
import pprint
import os
import urllib.parse
from flask import Flask, redirect, session, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import psycopg2


#initializing the app as Flask class
app = Flask(__name__)

#making connection to the postgres database with the role of the developer

conn = psycopg2.connect('host=172.17.0.2 dbname=stocks user=developer4 password=dev_pswd')
cur = conn.cursor()
conn.set_session(autocommit=True)


#sess dictionary will carry the temporal information about the user across the functions
sess = {}
api_key = "pk_f99acd61740946c9b13696784a19452e" #API Key to IEX API
# Here is the page to the documentation to IEX API https://iexcloud.io/docs/api/


@app.route('/')
def hello():
        return "<h1>Welcome to QMUL Stocks Trading!</h1>", 200

@app.route('/stocks/<symbol>', methods=['GET'])
def get_records(symbol):
        '''
        symbol: Pass the symbol of the stock as an endpoint
        return: displays the stock's name, price and symbol
        '''
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
        '''
        return: the function is for the user to register for the account
        '''
        new_user = {'name': request.json['name'], 'pswd': generate_password_hash(request.json['pswd'])}
        cur.execute('''INSERT INTO stocks.users (username, hash) VALUES (%s, %s)''', (new_user['name'], new_user['pswd']))
        return jsonify({'message': 'Account registered: {}'.format(request.json['name'])}), 200

@app.route("/login", methods=["POST"])
def login():
        '''
        return: this function is for the user to login
        '''
        user = {'name': request.json['name'], 'pswd': request.json['pswd']}
        cur.execute('''SELECT * FROM stocks.users WHERE username = (%s)''', (user['name'], ))
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
        '''
        this function is to user reset password
        '''
        user = {'name': request.json['name'], 'pswd': request.json['pswd'], 'new_pswd': generate_password_hash(request.json['new_pswd'])}
        cur.execute('''SELECT * FROM stocks.users WHERE username = (%s)''', (user['name'], ))
        row = cur.fetchall()
        if check_password_hash(row[0][2], user['pswd']):
                cur.execute('''UPDATE stocks.users SET hash =(%s)''', (user['new_pswd'], ))
                return jsonify("Password changed! ".format(user['name']))
        else:
                return jsonify("Incorrect credentials!"), 401

@app.route("/buy/<symbol>", methods=["POST"])
def buy(symbol):
        '''
        this function is to buy the stocks
        symbol: which stock with symbol to buy
        return: new stock details will be added to their page after making the post request
        '''
        url = f"https://cloud-sse.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        quote = response.json()
        time1 = datetime.now()
        try:
                cur.execute('''INSERT INTO stocks.sales (symbol, price, user_name, share_name) VALUES (%s, %s, %s, %s)''',
                (quote["symbol"] , float(quote["latestPrice"]), sess['name'], quote["companyName"]))
                return jsonify("Bought! {} at {} for {}".format(quote["companyName"], float(quote["latestPrice"]), sess['name'])), 201
        except KeyError:
                return jsonify("Kindly register or login first!"), 404

@app.route("/records", methods=["GET"])
def display_records():
        '''
        this function displays the records of stocks of the logged in user
        '''
        try:
                cur.execute('''SELECT * FROM stocks.sales WHERE user_name = (%s)''', (sess['name'], ))
                return jsonify(cur.fetchall()), 200
        except KeyError:
                return jsonify("Kindly register or login first!"), 404

@app.route("/return/<r_id>", methods=['DELETE'])
def return_stocks(r_id):
        '''
        r_id: ID of the stock that user wants to return
        return: after making this delete request, the stock will be deleted from the display page of the user
        '''
        cur.execute("""DELETE FROM stocks.sales WHERE id = {}""".format(r_id))
        return jsonify("Success!"), 200


if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
        print('tearing down')
        conn.close()
