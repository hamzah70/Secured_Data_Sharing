# Secured Data Movement
# User Interface - Hospital

import mysql.connector as sql
from RingFence import rid,ring_fence
import pickle

db = sql.connect(user='root', passwd='password',host='localhost')

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
	cursor=db.cursor()
	query="use Hospital;"
	cursor.execute(query)
	db.commit()
	cursor.close()
	cursor=db.cursor()
	command = "select Document from RID where id = '"+str(ridNumber)+"';"
	cursor.execute(command)
	data = cursor.fetchall()
	cursor.close()
	loadData = pickle.loads(data[0][0])

	cursor=db.cursor()
	command = "select * from Patients where rid = '"+str(ridNumber)+"';"
	cursor.execute(command)
	data = cursor.fetchall()

	args = {}
	for i in range(len(cursor.description)):
		label = cursor.description[i][0]
		value = data[0][i]
		if label!="RID":
			args[label]=value

	cursor.close()
	r = ring_fence(loadData)
	r.create(args)

	return r

print(fetchData("bb758087-3426-11eb-bc7c-000000000001").getID())