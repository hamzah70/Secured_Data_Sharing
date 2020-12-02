def registerUser():
	print("Registering User...")

	with open("Input.txt","r") as file:
		Lines = file.readlines()
		Data = {}
		for x in Lines:
			x = x.strip()
			label,value = x.split(":")
			Data[label]=value

		print("Generating RID...")

		RID = rid("Policy_Hospital")
		Data["RID"]= RID.getuniqueID()
		Document = pickle.dumps(RID)

	file.close()

	query="use Hospital;"
	cursor.execute(query)
	db.commit()

	query = "insert into RID values (%s,%s)"
	cursor.execute(query,(Data["RID"],Document))
	db.commit()

	# @ Himanshu
	# query = "insert into Patients values ?"
	# cursor.execute(query,?)
	# db.commit()

	print("Registration Completed.")
	print("RID : ",Data["RID"])