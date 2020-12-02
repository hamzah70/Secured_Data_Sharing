# Secured Data Movement
# RID Population

import pickle
from RingFence import rid
import mysql.connector as sql

db = sql.connect(user='root', passwd='himraj18',host='localhost')
cursor=db.cursor()

query="use Hospital;"
cursor.execute(query)
db.commit()

query="drop table if exists RID;"
cursor.execute(query)
db.commit()

query="create table RID (ID TEXT, Document BLOB);"
cursor.execute(query)
db.commit()

query="SELECT * FROM Patients;"
cursor.execute(query)
data = cursor.fetchall()

Documents = {}

for i in range(50):
    x = rid("../Policies/Policy_Hospital.txt")
    data[i] = list(data[i])
    data[i][1] = str(x.getID())
    data[i] = tuple(data[i])
    Documents[str(x.getID())] = pickle.dumps(x)

query="delete from Patients;"
cursor.execute(query)
db.commit()

query="insert into Patients value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
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

db = sql.connect(user='root', passwd='himraj18',host='localhost')
cursor=db.cursor()

query="use Insurance;"
cursor.execute(query)
db.commit()

query="drop table if exists RID;"
cursor.execute(query)
db.commit()

query="create table RID (ID TEXT, Document BLOB);"
cursor.execute(query)
db.commit()

query="SELECT * FROM Insurance;"
cursor.execute(query)
data = cursor.fetchall()

Documents = {}

for i in range(20):
    x = rid("../Policies/Policy_Insurance.txt")
    data[i] = list(data[i])
    data[i][1] = str(x.getID())
    data[i] = tuple(data[i])
    Documents[str(x.getID())] = pickle.dumps(x)

query="delete from Insurance;"
cursor.execute(query)
db.commit()

query="insert into Insurance value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
cursor.executemany(query,data)
db.commit()

query = "insert into RID values (%s,%s)"
for i in Documents:
    cursor.execute(query,(i,Documents[i]))
    db.commit()