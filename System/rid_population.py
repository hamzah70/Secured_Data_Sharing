# Secured Data Movement
# RID Population

import pickle
from RingFence import rid
import mysql.connector as sql

db = sql.connect(user='root', passwd='password',host='localhost')

cursor=db.cursor()
query="use Mediator;"
cursor.execute(query)
db.commit()

query="drop table if exists Agreement;"
cursor.execute(query)
db.commit()

query="create table Agreement (A TEXT,B TEXT, Agreement BLOB, Code BLOB);"
cursor.execute(query)
db.commit()
cursor.close()

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

query="insert into Patients value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
cursor.executemany(query,data)
db.commit()

query = "insert into RID values (%s,%s)"
for i in Documents:
    cursor.execute(query,(i,Documents[i]))
    db.commit()

query = "delete from Mediator.RID;"
cursor.execute(query)
db.commit()

query = "insert into Mediator.RID select * from Hospital.RID;"
cursor.execute(query)
db.commit()

cursor.close()
    
# query = "SELECT ID, Document FROM RID"
# cursor.execute(query)
# for a,b in cursor.fetchall():
#     print (a,pickle.loads(b).getKeys())

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
cursor.close()

cursor=db.cursor()
query="SELECT * FROM Insurance;"
cursor.execute(query)
data = cursor.fetchall()
cursor.close()

Documents = {}

for i in range(20):
    x = rid("../Policies/Policy_Insurance.txt")
    data[i] = list(data[i])
    data[i][1] = str(x.getID())
    data[i] = tuple(data[i])
    Documents[str(x.getID())] = pickle.dumps(x)

cursor=db.cursor()
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

query = "insert into Mediator.RID select * from Insurance.RID;"
cursor.execute(query)
db.commit()

cursor.close()


cursor = db.cursor()
query = "select Name, RID from Hospital.Patients order by Name;"
cursor.execute(query)
H = cursor.fetchall()
cursor.close()


cursor = db.cursor()
query = "select Name,RID from Insurance.Insurance order by Name;"
cursor.execute(query)
I = cursor.fetchall()

Data = []
for x in I:
    for y in H:
        if x[0]==y[0]:
           Data.append((x[1],y[1]))
           Data.append((y[1],x[1]))

query = "insert into Mediator.agreement values (%s,%s,null,null)"
for i in range(len(Data)):
    cursor.execute(query,Data[i])
    db.commit()


# query = "SELECT ID, Document FROM RID"
# cursor.execute(query)
# for a,b in cursor.fetchall():
#     print (a,pickle.loads(b).getKeys())


