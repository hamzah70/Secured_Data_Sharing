# Secured Data Movement
# User Interface - Insurance

import mysql.connector as sql

db = sql.connect(user='root', passwd='password',host='localhost')

def getRID():
	print("Enter RID:  ")
	ans = input()
	return ans
