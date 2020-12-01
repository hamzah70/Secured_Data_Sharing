# Secured Data Movement
# Mediator Transaction

from flask import Flask, render_template, redirect, url_for,request, jsonify, session
from flask import make_response
import mysql.connector
from mysql.connector import Error
import requests


app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def sendHospital():
# 	print("hello")
# 	r = requests.post('http://0.0.0.0:6000/', data = {'image_filename':'test.jpg', 'image_url': "http://images.come"}, verify=False)
# 	return "abc"

@app.route('/getRID', methods=['GET', 'POST'])
def getRIDInsurance():
	if request.method == 'POST':
		result = request.form
		ridNumber = result["rid"]
		val = verifyRID(ridNumber)
		if val==1:
			r = requests.post('https://0.0.0.0:6000/', data = {"rid": ridNumber}, verify=False)
		if val==0:
			print("data not found")
	return "abc"


@app.route('/getRF', methods=['GET', 'POST'])
def getHospitalRID():
	if request.method == 'POST':
		result = request.form['result']
		x = functional(result.dissolve)
		requests.post('https://0.0.0.0:6000/get', data = {"x": x}, verify=False)
	return "Abc"


def verifyRID(ridNumber):
	db = sql.connect(user='root', passwd='&TDj6j7>',host='localhost')
	cursor=db.cursor()

	query="use Mediator;"
	cursor.execute(query)
	db.commit()

	command = "select exists (select * from RID where id=" + ridNumber + ");"
	cursor.execute(command)
	db.commit()
	val = cursor.fetchall()
	return val


if __name__ == "__main__":

	# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
	app.run(host='0.0.0.0', port="6000", debug=True,ssl_context=('cert.pem', 'key.pem'))
