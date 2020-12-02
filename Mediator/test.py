

import mysql.connector as sql

db = sql.connect(user='root', passwd='password',host='localhost')
cursor=db.cursor()

query="use DBMS;"
cursor.execute(query)
db.commit()

query="SELECT * FROM Guardian where GID = 'GID0000600';"
cursor.execute(query)
data = cursor.fetchall()


for i in range(len(cursor.description)):
	label = cursor.description[i][0]
	value = data[0][i]
	print(label,value)



print(data[0][0])