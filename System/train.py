# Secured Data Movement
# ML Training

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

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