# Secured Data Movement
# Mediator Transaction

from flask import Flask, render_template, redirect, url_for,request, jsonify, session
from flask import make_response
import mysql.connector
from mysql.connector import Error
import requests
from insurance import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sendMediator():
	ridNumber = getRID()
	r = requests.post('https://0.0.0.0:6000/getRID', data = {"rid": ridNumber}, verify = False)
	return "abc"

@app.route('/get', methods=['GET', 'POST'])
def getMediator():
	if request.method == 'POST':
		x = request.form['x']
		print(" final result  :    ", x)
	return "abc"

if __name__ == "__main__":
	# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
	app.run(host='0.0.0.0', port="5000", debug=True, ssl_context=('cert.pem', 'key.pem'))
	ridNumber = getRID()
	r = requests.post('https://0.0.0.0:6000/getRID', data = {"rid": ridNumber}, verify = False)
