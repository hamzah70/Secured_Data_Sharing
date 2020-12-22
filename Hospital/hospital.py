# Secured Data Movement
# User Interface - Hospital

import pickle
import mysql.connector as sql
from RingFence import rid,ring_fence


db = sql.connect(user='root', passwd='password',host='localhost')

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
	RID = pickle.loads(data[0][1])
	cursor.close()

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

	r = ring_fence(RID)
	r.create(args,1)

	return r
