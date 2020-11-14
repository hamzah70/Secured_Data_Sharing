# Secured Data Movement
# Hospital Transaction


from flask import Flask, render_template, redirect, url_for,request, jsonify, session
from flask import make_response
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def getMediator():
	if request.method == 'POST':
		result = request.form
		print("\n\n\n\n")
		print(result["image_filename"])
		print("\n\n\n\n")
		print(result["image_url"])
	return "abc"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port="8080", debug=True)