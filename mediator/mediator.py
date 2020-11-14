# Secured Data Movement
# Mediator Transaction

from flask import Flask, render_template, redirect, url_for,request, jsonify, session
from flask import make_response
import mysql.connector
from mysql.connector import Error
import requests


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sendHospital():
	print("hello")
	r = requests.post('http://0.0.0.0:8080/', data = {'image_filename':'test.jpg', 'image_url': "http://images.come"})
	return "abc"

@app.route('/createdid', methods=['GET', 'POST'])
def createDiD():
	if request.method == 'POST':
		result = request.form


if __name__ == "__main__":
	app.run(host='0.0.0.0', port="5000", debug=True)