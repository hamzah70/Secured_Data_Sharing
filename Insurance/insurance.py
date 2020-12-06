# Secured Data Movement
# User Interface - Insurance

import mysql.connector as sql

db = sql.connect(user='root', passwd='password',host='localhost')

def getRID():
	print("--------------------------------------------------------")
	print("Enter RID:  ")
	print("--------------------------------------------------------")
	print()
	ans = input()
	return ans
