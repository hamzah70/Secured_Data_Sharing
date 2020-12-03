# Secured Data Movement
# Mediator Transaction

from flask import Flask, render_template, redirect, url_for,request, jsonify, session
from flask import make_response
from mysql.connector import Error
import mysql.connector
import requests
from hospital import *
from json import dumps as jsonstring
import pickle
import jsonpickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def transaction():
	if request.method == 'POST':
		result = request.form
		ridNumber = result["rid"]
		result = fetchData(ridNumber)
		print("printing")
		# print(result.getBlock())
		# result = jsonstring(result.__dict__)
		# print(result)
		result = result.__dict__
		# result = pickle.dumps(result)
		# result = jsonpickle.encode(result)
		print(result)
		r = requests.post('https://0.0.0.0:6000/getRF', data = result, verify=False)
	return "abc"

if __name__ == "__main__":
	# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
	app.run(host='0.0.0.0', port="7000", debug=True, ssl_context=('cert.pem', 'key.pem'))