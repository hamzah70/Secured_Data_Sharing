
import mysql.connector as sql
import pickle

db = sql.connect(user='root', passwd='password',host='localhost')

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
cursor.close()