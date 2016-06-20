#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, Response, request
from bs4 import BeautifulSoup
import urllib2
import requests
import simplejson
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def waterflow():
	token = 'oMIDPAKrLgAvVogcR96f4sDi'

	#check if valid request
	if 'token' not in request.args:
		return ''
	if request.args.get('token') != token:
		return ''

	#check if loc is defined
	if 'text' not in request.args:
		return "Hvilket vassdrag vil du vite vannføringen i?. Bruk '/vannføring [vassdrag]'."

	#get input from slack
	vassdrag = request.args.get('text').lower()

	#check if drammen
	if 'drammen' in vassdrag.lower():
		return 'LaksBot støtter ikke Drammen og omegn.'

	#basic url
	base_url = 'http://www2.nve.no/h/hd/plotreal/Q/'
	list_url = base_url + 'list.html'

	
	#Build dict of place / uri pairs
	soup = BeautifulSoup(urllib2.urlopen(list_url).read(),'html.parser')
	table = soup.find('table')
	rows = table.findAll('tr')
	river = {}
	for tr in rows:
		link = tr.find('a', href=True)
		river[link.text.lower()] = link['href'][:-11]

	if vassdrag not in river:
		return "Ukjent vassdrag."


	#create response dict
	attachments = {}
	attachments['image_url'] =  base_url + river[vassdrag] + '/plot.gif' 
	output = {}
	output['response_type'] = 'in_channel'
	output['text'] = vassdrag.title() + ':'
	output['attachments'] = [attachments]

	json_response = json.dumps(output)

	resp = Response(response=json_response, status=200, mimetype="application/json")
	
	return resp

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)