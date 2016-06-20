from flask import Flask, jsonify, Response, request
import requests
import simplejson
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
	return "Hello world"

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)