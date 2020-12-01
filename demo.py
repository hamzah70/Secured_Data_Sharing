# Secured Data Movement
# User Interface

import mysql.connector as sql
from RingFence import rid

db = sql.connect(user='root', passwd='&TDj6j7>',host='localhost')
cursor=db.cursor()

with open("Input.txt","r") as file:
	Lines = file.readlines()
	Data = {}
	for x in Lines:
		x = x.strip()
		label,value = x.split(":")
		Data[label]=value
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
