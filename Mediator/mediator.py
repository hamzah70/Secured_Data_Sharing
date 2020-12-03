# Secured Data Movement
# Mediator

import pickle
import numpy as np
import pandas as pd
import mysql.connector as sql
from sklearn.tree import DecisionTreeRegressor


db = sql.connect(user='root', passwd='scorpio',host='localhost', database='Mediator')

def resolve(R):
	print("resolve")
	ridNumber = R.getBlock()["MetaData"]["RID"]
	cursor = db.cursor()
	command = """select Document from RID where ID =%s);"""
	cursor.execute(command, (ridNumber,))
	data = cursor.fetchall()
	db.commit()
	cursor.close()

	loadData = pickle.loads(data[0][0])
	val = loadData.getKeys()
	return predict(R.dissolve(val))

def verifyRID(ridNumber):

	cursor=db.cursor()
	print("hello")
	print(ridNumber)

	command = """select exists (select * from RID where ID =%s);"""
	# params = str(ridNumber)
	cursor.execute(command, (ridNumber,))
	val = cursor.fetchall()[0][0]
	db.commit()
	
	cursor.close()

	return val

def load_model(filename="insurance_ML_model.pkl"):

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

def predict(inp):

	X = preprocess_input(inp)
	clf = load_model()

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



