# Secured Data Movement
# Mediator Transaction

from flask import Flask, render_template, redirect, url_for,request, jsonify, session
from flask import make_response
from mysql.connector import Error
import mysql.connector
import requests
from hospital import *
import json
import pickle
import jsonpickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def transaction():
	headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
	if request.method == 'POST':
		result = request.form
		ridNumber = result["rid"]
		result = fetchData(ridNumber)
		result = json.dumps(jsonpickle.encode(result))
		r = requests.post('https://0.0.0.0:4000/getRF', data = result, verify=False, headers=headers)
	return "Hospital Server"

if __name__ == "__main__":
	# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
	app.run(host='0.0.0.0', port="7000", debug=True, ssl_context=('cert.pem', 'key.pem'))