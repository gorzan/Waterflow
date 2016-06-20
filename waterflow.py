from flask import Flask, jsonify, Response, request
import requests
import simplejson
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def waterflow():

	#create response dict
	output = {}
	output['response_type'] = 'in_channel'
	output['text'] = 'Test av vannstrøm'

	json_response = json.dumps(output)

	resp = Response(response=json_response, status=200, mimetype="application/json")
	
	return resp

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)