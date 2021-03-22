import requests
import pprint
import os
import urllib.parse
from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route('/')
def hello():
	return "<h1>Welcome to Cloud Merchandise!</h1>"

 
@app.route('/getfilms', methods=['GET'])
def getfilms():
    #send a get request to the following url
    resp = requests.get('https://ghibliapi.herokuapp.com/films')
    
    
    if resp.ok:
        return jsonify(resp.json())
    else:
        print(resp.reason)




@app.route('/getfilms/all_titles', methods=['GET'])
def getfilms_allTitles():
    #send a get request to the following url
    resp = requests.get('https://ghibliapi.herokuapp.com/films')

    titles = []
    if resp.ok:
        content = resp.json()
        for di in content:
            titles.append(di["title"])
        return jsonify(titles)
    else:
        print(resp.reason)

@app.route('/getfilms/producers/', methods=['GET'])

def get_producers():
  resp= requests.get('https://ghibliapi.herokuapp.com/films')
  if resp.ok:
   data= resp.json()
   response = [item['producer'] for item in data ]
   return jsonify(response)
  else:
    print(resp.reason)


@app.route('/getfilms/all_titles/<title>', methods=['GET'])
def getTitle(title):
    resp = requests.get('https://ghibliapi.herokuapp.com/films')
    if resp.ok:
       data= resp.json()
       title = [item['title'] for item in data if item['title'] == title]
       if len(title)==0:
         return jsonify({'error':'Title not found!'}), 404 
       else:
         return jsonify(title)
    
@app.route('/getfilms/<add_title>', methods=['post'])
def Create_Title():
 resp = requests.get('https://ghibliapi.herokuapp.com/films')
 data =resp.json()
 if not data  or not 'title' in data:
   return jsonify({'error':'the new title cannot be added' }), 400
 new_tile = {
 'title': data['title']
 
}
 res.append(new_title)
 return jsonify({'message': 'created: /getfilms/{}'.format(new_title['title'])}), 201
# method not allowed, 405 

if __name__=="__main__":
    app.run(debug =True)

