# Secured Data Movement
# Mediator Transaction

from flask import Flask, render_template, redirect, url_for,request, jsonify, session
from flask import make_response
from mysql.connector import Error
import mysql.connector
import requests
from Hospital_UI import *

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def sendMediator():
# 	print("hello")
# 	r = requests.post('http://0.0.0.0:8080/', data = {'image_filename':'test.jpg', 'image_url': "http://images.come"})
# 	return "abc"

@app.route('/', methods=['GET', 'POST'])
def retrieve_send_RID():
	if request.method == 'POST':
		result = request.form
		ridNumber = result["rid"]
		result = fetchData(ridNumber)
		r = requests.post('https://0.0.0.0:6000/getRF', data = {'result':result}, verify=False)
	return "abc"




if __name__ == "__main__":

	# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
	app.run(host='0.0.0.0', port="7000", debug=True, ssl_context=('cert.pem', 'key.pem'))