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

query="drop table if exists RID;"
cursor.execute(query)
db.commit()

query="create table RID (ID TEXT, Document BLOB);"
cursor.execute(query)
db.commit()

query="SELECT * FROM hospital;"
cursor.execute(query)
data = cursor.fetchall()

Documents = {}

for i in range(50):
    x = rid("Policy_Hospital.txt")
    data[i] = list(data[i])
    data[i][1] = str(x.getID())
    data[i] = tuple(data[i])
    Documents[str(x.getID())] = pickle.dumps(x)

query="delete from hospital;"
cursor.execute(query)
db.commit()

query="insert into hospital value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
cursor.executemany(query,data)
db.commit()

query = "insert into RID values (%s,%s)"
for i in Documents:
    cursor.execute(query,(i,Documents[i]))
    db.commit()
    
# query = "SELECT ID, Document FROM RID"
# cursor.execute(query)
# for a,b in cursor.fetchall():
#     print (a,pickle.loads(b).getID())