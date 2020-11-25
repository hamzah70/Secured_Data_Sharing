# Secured Data Movement
# ML Model 

import pickle
import numpy as np
import pandas as pd
import mysql.connector as sql
from sklearn.tree import DecisionTreeRegressor

def apply_DT(X, Y):

	# X_train, X_test = X[:int(0.8*len(X))], X[int(0.8*len(X)):]
	# Y_train, Y_test = Y[:int(0.8*len(Y))], Y[int(0.8*len(Y)):]
	# clf = DecisionTreeRegressor()
	# clf.fit(X_train, Y_train)
	# print(clf.score(X_test, Y_test))
	# return clf

	clf = DecisionTreeRegressor()
	clf.fit(X, Y)
	print(clf.score(X, Y))
	return clf


def sep_X_Y(df):

	cols=df.columns
	X = df[cols[:-1]].to_numpy()
	Y = df[cols[-1]].to_numpy()
	return X,Y

# db_connection = sql.connect(user='root', passwd='himraj18',host='localhost', database = "ip")
# db_cursor = db_connection.cursor()
# db_cursor.execute('show columns FROM hospital')
# table_col = db_cursor.fetchall()
# table_col = [i[0] for i in table_col]
# db_cursor.execute('SELECT * FROM hospital')
# table_rows = db_cursor.fetchall()
# df = pd.DataFrame(table_rows, columns = table_col)
# df.to_csv('patients.csv',index=False)
# print(df)

def train_model():

	df = pd.read_csv('patients.csv')
	cm1 = df.columns
	remove_cols = [0,1,2,4,5,6,7,8,9,10,11,12,13,14,16,17,19,20,21,22,23,24,25,28]
	df.columns = [i for i in range(40)]

	df = df.drop(remove_cols, axis=1)
	cm2 = df.columns
	final_cols = []

	for i in range(len(cm2)):
		final_cols.append(cm1[cm2[i]])

	print(final_cols)
	df = df.fillna(0)
	df = df.apply (pd.to_numeric, errors='coerce')
	df = df.fillna(1)

	X,Y = sep_X_Y(df)
	clf = apply_DT(X,Y)
	pickle_out = open("insurance_ML_model.pkl","wb")
	pickle.dump(clf,pickle_out)


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