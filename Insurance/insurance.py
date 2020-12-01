# Secured Data Movement
# User Interface - Insurance

import mysql.connector as sql
from RingFence import rid

db = sql.connect(user='root', passwd='&TDj6j7>',host='localhost')
cursor=db.cursor()

def registerUser():

	print("Registering User...")

	with open("Input.txt","r") as file:
		Lines = file.readlines()
		Data = {}
		for x in Lines:
			x = x.strip()
			label,value = x.split(":")
			Data[label]=value

		print("Generating RID...")

		RID = rid("Policy_Insurance")
		Data["RID"]= RID.getuniqueID()
		Document = pickle.dumps(RID)

	file.close()

	query="use Insurance;"
	cursor.execute(query)
	db.commit()

	query = "insert into RID values (%s,%s)"
	cursor.execute(query,(Data["RID"],Document))
	db.commit()

	# @ Himanshu
	# query = "insert into Insurance values ?"
	# cursor.execute(query,?)
	# db.commit()

	print("Registration Completed.")
	print("RID : ",Data["RID"])


	print("1 : Know Best Policy For Yourself")
	print("2 : Exit")

	n = int(input())

	if n == 1:
		print("Enter Your Hospital RID")
		x = input()

		#@Hamzah Send it to mediator!

		# y = recieve from mediator

		print(y)

	else:
		print("Thank You.")
		sys.exit(0)

def getRID():
	
	print("Enter RID for a person you want best policy:  ")
	ans = input()
	return ans
