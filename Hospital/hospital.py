# Secured Data Movement
# User Interface - Hospital

import mysql.connector as sql
from RingFence import rid
import pickle

db = sql.connect(user='root', passwd='&TDj6j7>',host='localhost')

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

		RID = rid("Policy_Hospital")
		Data["RID"]= RID.getuniqueID()
		Document = pickle.dumps(RID)

	file.close()

	query="use Hospital;"
	cursor.execute(query)
	db.commit()

	query = "insert into RID values (%s,%s)"
	cursor.execute(query,(Data["RID"],Document))
	db.commit()

	# @ Himanshu
	# query = "insert into Patients values ?"
	# cursor.execute(query,?)
	# db.commit()

	print("Registration Completed.")
	print("RID : ",Data["RID"])

def fetchData(ridNumber):
	query="use Hospital;"
	cursor.execute(query)
	db.commit()

	cursor=db.cursor()
	command = "select Document from RID where id='"+ridNumber+"';"
	cursor.execute(command)
	db.commit()
	data = cursor.fetchall()
	cursor.close()
	loadData = pickle.loads(data[0][0])

	cursor=db.cursor()
	command = "select * from Patients where rid="+ridNumber+";"
	cursor.execute(command)
	db.commit()
	data = cursor.fetchall()
	cursor.close()

	args = {}
	for i in range(len(cursor.description)):
		label = cursor.description[i][0]
		value = data[0][i]
		if label!="RID":
			args[label]=value

	r = RingFence(loadData)
	r.create(args)

	return r

print(fetchData("bb758087-3426-11eb-bc7c-000000000001"))