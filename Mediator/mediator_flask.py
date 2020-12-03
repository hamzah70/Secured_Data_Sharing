# Secured Data Movement
# Mediator Transaction

from flask import Flask, render_template, redirect, url_for,request, jsonify, session
from flask import make_response
import mysql.connector
from mysql.connector import Error
import requests
from mediator import *
from json import loads
import ast
import pickle
import jsonpickle

app = Flask(__name__)

@app.route('/getRID', methods=['GET', 'POST'])
def getInsurance():
	print("Were in")
	if request.method == 'POST':
		result = request.form
		ridNumber = result["rid"]
		val = verifyRID(ridNumber)
		if val==1:
			print("found everything")
			r = requests.post('https://0.0.0.0:7000/', data = {"rid": ridNumber}, verify=False)
		else :
			print("data not found")
	return "abc"


@app.route('/getRF', methods=['GET', 'POST'])
def getHospital():
	if request.method == 'POST':
		print("hello")
		print(request.form)
		result = pickle.loads(request.get_data())
		# result = jsonpickle.decode(request.get_data())
		print("HOSRES")
		print(result)
		print(result.getBlock())
		x = resolve(result)
		requests.post('https://0.0.0.0:5000/get', data = {"x": x}, verify=False)
	return "Abc"


if __name__ == "__main__":
	# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
	app.run(host='0.0.0.0', port="6000", debug=True,ssl_context=('cert.pem', 'key.pem'))
