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
	command = "select ID, Document from RID where id = '"+str(ridNumber)+"';"
	cursor.execute(command)
	data = cursor.fetchall()
	cursor.close()
	loadData = pickle.loads(data[0][1])
	print(loadData.getKeys())
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

#X = fetchData("4e540efa-3465-11eb-b729-000000000001")

cursor=db.cursor()
query="use Hospital;"
cursor.execute(query)
db.commit()
cursor.close()


cursor=db.cursor()
query = "SELECT ID, Document FROM RID"
cursor.execute(query)
for a,b in cursor.fetchall():
    print (a,pickle.loads(b).getSharedData())
# command = "select Document from RID where id = '"+"4e540efa-3465-11eb-b729-000000000001"+"';"
# cursor.execute(command)
# data = cursor.fetchall()
# cursor.close()
# loadData = pickle.loads(data[0][0])
# print(loadData.getKeys())
# print(X.dissolve(loadData.getKeys()))