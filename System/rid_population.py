# Secured Data Movement
# RID Population

import pickle
from RingFence import rid
import mysql.connector as sql

db = sql.connect(user='root', passwd='&TDj6j7>',host='localhost')
cursor=db.cursor()

query="use ip;"
cursor.execute(query)
db.commit()

query="create table RID (ID TEXT, Document BLOB);"
cursor.execute(query)
db.commit()

Documents = {}

for i in range(50):
	x = rid("Policy_Hospital.txt")
	Documents[str(x.getuniqueID)] = pickle.dumps(x)

query = "insert into RID values (%s,%s)"
for i in Documents:
	cursor.execute(query,(i,Documents[i]))
	db.commit()
	
# query = "SELECT ID, Document FROM RID"
# cursor.execute(query)
# for a,b in cursor.fetchall():
#     print (a,pickle.loads(b).uniqueID)