# Secured Data Movement
# Mediator Transaction

from flask import Flask, render_template, redirect, url_for,request, jsonify, session
from flask import make_response
import mysql.connector
from mysql.connector import Error
import requests
from mediator import *
import json
import ast
import pickle
import jsonpickle

app = Flask(__name__)

@app.route('/getRID', methods=['GET', 'POST'])
def getInsurance():
	if request.method == 'POST':
		result = request.form
		ridNumber = result["rid"]
		rid = int(ridNumber)
		if rid != 0:
			r = requests.post('https://0.0.0.0:7000/', data = {"rid": rid}, verify=False)
		else :
			print("- Request Rejected -")
	return "Mediator Server"


@app.route('/getRF', methods=['GET', 'POST'])
def getHospital():
	if request.method == 'POST':
		result = jsonpickle.decode(json.loads(request.get_data()))
		if result!="None":
			D, ridNumber = extract(result)
		else:
			print("\n\nData not found\n\n")
		x = resolve(D,ridNumber)
		requests.post('https://0.0.0.0:5000/get', data = {"x": x}, verify=False)
	return "Mediator Server"


if __name__ == "__main__":
	# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
	app.run(host='0.0.0.0', port="5001", debug=True,ssl_context=('cert.pem', 'key.pem'))
