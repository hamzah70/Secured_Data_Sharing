# Secured Data Movement
# User Interface - Insurance

import mysql.connector as sql

db = sql.connect(user='root', passwd='scorpio',host='localhost')

def getRID():
	print("Enter RID:  ")
	ans = input()
	return ans
