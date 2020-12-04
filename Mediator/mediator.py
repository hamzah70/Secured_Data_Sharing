# Secured Data Movement
# Mediator

import pickle
import numpy as np
import pandas as pd
import mysql.connector as sql
from sklearn.tree import DecisionTreeRegressor


db = sql.connect(user='root', passwd='password',host='localhost', database='Mediator')

def verify(ridNumber):

	cursor=db.cursor()
	query = "select exists (select * from Agreement where B = '"+str(ridNumber)+"');"
	cursor.execute(query)
	val = cursor.fetchall()[0][0]
	if val :
		query = "select A from Agreement where B = '"+str(ridNumber)+"';"
		cursor.execute(query)
		r = cursor.fetchall()[0][0]
		print("[~] Request Verified!")
	else:
		r = 0
	cursor.close()
	return r

def extract(R):
	
	ridNumber = str(R.getBlock()["MetaData"]["RID"])
	cursor = db.cursor()
	query = "select Document from RID where ID ='"+str(ridNumber)+"';"
	cursor.execute(query)
	data = cursor.fetchall()[0][0]
	cursor.close()

	Document = pickle.loads(data)
	keys = Document.getKeys()

	return R.dissolve(keys,1), ridNumber

def resolve(D,ridNumber):

	cursor = db.cursor()
	query = "select Code from Agreement where A = '"+str(ridNumber)+"';"
	cursor.execute(query)
	data = cursor.fetchall()[0][0]
	cursor.close()

	clf = load_model(data)
	return predict(D,clf)

def load_model(filename="ML_model.pkl"):
	pickle_in = open(filename,"rb")
	clf = pickle.load(pickle_in)
	return clf

def preprocess_input(inp):
	cols = ['Age', 'Physical_Disability', 'Allergies', 'Haemoglobin_Level', 'Vitamin_Deficiency', 'Cancer_Stage', 'Heart_Disease', 'Diabetic', 'Surgeries', 'Organ_Replacement', 'Fractures', 'Alcoholic', 'Smoker', 'Drug_Abuse', 'Rehab']
	X = [[]]

	for i in cols:
		if(i in inp):
			X[0].append(inp[i])
		else:
			X[0].append(None)

	df = pd.DataFrame(data = X)
	df = df.fillna(0)
	df = df.apply(pd.to_numeric, errors='coerce')
	df = df.fillna(1)
	X = df.to_numpy()

	return X

def predict(inp,clf):
	X = preprocess_input(inp)
	temp = clf.predict(X)[0]
	
	if(temp < 250000):
		return 1
	elif(temp < 500000):
		return 2
	elif(temp < 750000):
		return 3
	elif(temp < 1000000):
		return 4
	elif(temp < 1500000):
		return 5
	else:
		return 6

#test1 = {'Age' : 50, 'Physical_Disability': 'Amputation', 'Allergies' : None, 'Haemoglobin_Level' : 9.0, 'Vitamin_Deficiency': 'Vitamin A Deficient', 'Cancer_Stage' : 2, 'Heart_Disease' : 1, 'Diabetic' : 1, 'Surgeries' : 'Open Heart Surgery', 'Organ_Replacement' : 'Liver Transplant', 'Fractures' : 'Leg Fracture', 'Alcoholic' : 1, 'Smoker' : 1, 'Drug_Abuse' : 1, 'Rehab' : 1}
#print(predict(test1)) 

#"d171d2d0-3669-11eb-87db-00000000328a"

print(verify("d171d2d0-3669-11eb-87db-00000000328a"))