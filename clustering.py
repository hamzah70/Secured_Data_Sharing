# Secured Data Movement
# Data Clusters

'''
	Categorising the different data attributes and forming clusters of attributes of similar type.
'''

Hospital_Clusters = 
{
	"Personal_Details" : ["Name","Age","Gender"],
	"Contact_Details" : ["Email","Phone_Number","Address"],
	"Medical_Records_1" : ["Allergies","Vitamin_Deficiency","Diabetic"],
	"Medical_Records_2" : ["Heart_Rate","Blood_Pressure","Blood_Oxygen","Body_Fat","Respiratory_Rate","Cholestrol_Level","Haemoglobin_Level","Sleep_Duration"],
	"Medical_Records_3" : ["Cancer_Type","Cancer_Stage","Heart_Disease","Organ_Replacement","Physical_Disability","Surgeries","Fractures"],
	"Addictions" : ["Alcoholic","Smoker","Drug_Abuse","Rehab"],
	"Confidential" : ["Email","Height","Weight","Last_Diagnosis_Report","Primary_Doctor","Patient_Number","Registeration_Date","Number_of_visits","Corporate_Coverage"]
}

Insurance_Clusters = 
{
	"Personal_Details" : ["Name","Age","Gender","Family_Members","Married"],
	"Contact_Details" : ["Phone_Number","Address"],
	"Financial_Details" : ["Occupation"],
	"Insurance_Details" : ["Policy_Number","Policy_Details","Period","Amount"],
	"Premium_Details": ["Premium","Premium_Paid","Premium_Overdue","Lock_In_Period","Previous_Claims"]
}