# Secured Data Movement
# RID Population

import pickle
from RingFence import rid
import mysql.connector as sql

db = sql.connect(user='root', passwd='password',host='localhost')

cursor=db.cursor()
query="use Hospital;"
cursor.execute(query)
db.commit()
cursor.close()

cursor=db.cursor()
query="drop table if exists RID;"
cursor.execute(query)
db.commit()
cursor.close()

cursor=db.cursor()
query="create table RID (ID TEXT, Document BLOB);"
cursor.execute(query)
db.commit()
cursor.close()

cursor=db.cursor()
query="SELECT * FROM Patients;"
cursor.execute(query)
data = cursor.fetchall()
cursor.close()

Documents = {}

for i in range(50):
    x = rid("../Policies/Policy_Hospital.txt")
    data[i] = list(data[i])
    data[i][1] = str(x.getID())
    data[i] = tuple(data[i])
    Documents[str(x.getID())] = pickle.dumps(x)

cursor=db.cursor()
query="delete from Patients;"
cursor.execute(query)
db.commit()
cursor.close()

cursor=db.cursor()
query="insert into Patients value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
cursor.executemany(query,data)
db.commit()
cursor.close()

cursor=db.cursor()
query = "insert into RID values (%s,%s)"
for i in Documents:
    cursor.execute(query,(i,Documents[i]))
    db.commit()
cursor.close()

cursor=db.cursor()    
query = "SELECT ID, Document FROM RID"
cursor.execute(query)
for a,b in cursor.fetchall():
    print (a,pickle.loads(b).getSharedData())
cursor.close()