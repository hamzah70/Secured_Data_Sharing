CREATE TABLE `hospital` (
	`Patient_Number` int NOT NULL,
	`Name` varchar(50) NOT NULL,
	`Age` int NOT NULL,
	`Gender` VARCHAR(10) NOT NULL,
	`Phone_Number` bigint NOT NULL,
	`Email` varchar(50) NOT NULL,
	`Address` varchar(50) NOT NULL,

	`Registeration_Date` date NOT NULL,
	`Primary_Doctor` varchar(50) DEFAULT NULL,
	`Corporate_Coverage` tinyint DEFAULT NULL,
	`Last_Visit` date DEFAULT NULL,
	`Last_Diagnosis` varchar(500) DEFAULT NULL,
	`Number_of_visits` int DEFAULT 0,

	`Blood_Group` varchar(5) NOT NULL,
	`Physical_Disability` varchar(100) DEFAULT NULL,
	`Height` int DEFAULT 0,
	`Weight` int DEFAULT 0,
	`Allergies` varchar(100) DEFAULT NULL,

	`Heart_Rate` float DEFAULT NULL,
	`Blood_Pressure` varchar(20) DEFAULT NULL,
	`Blood_Oxygen` float DEFAULT NULL,
	`Body_Fat` float DEFAULT NULL,
	`Respiratory_Rate` float DEFAULT NULL,
	`Cholestrol_Level` float DEFAULT NULL,
	`Sleep_Duration` float DEFAULT NULL,
	`Haemoglobin_Level` float DEFAULT NULL,
	`Vitamin_Deficiency` varchar(100) DEFAULT NULL,

	`Cancer_Type` varchar(100) DEFAULT NULL,
	`Cancer_Stage` int DEFAULT NULL,
	`Heart_Disease` tinyint DEFAULT NULL,
	`Diabetic` tinyint DEFAULT 0,

	`Surgeries` varchar(100) DEFAULT NULL,
	`Organ_Replacement` varchar(100) DEFAULT NULL,
	`Fractures` varchar(100) DEFAULT NULL,

	`Alcoholic` tinyint DEFAULT 0,
	`Smoker` tinyint DEFAULT 0,
	`Drug_Abuse` tinyint DEFAULT 0,
	`Rehab` tinyint DEFAULT 0,

	PRIMARY KEY (`Patient_Number`)
);

CREATE TABLE `insurance` (
	`Case_Number` int NOT NULL,
	`Name` varchar(50) NOT NULL,
	`Age` int NOT NULL,
	`Gender` VARCHAR(10) NOT NULL,
	`Phone_Number` bigint NOT NULL,
	`Family_Members` int NOT NULL,
	`Married` tinyint NOT NULL,
	`Occupation` varchar(50) NOT NULL,
	`Address` varchar(50) NOT NULL,

	`Policy_Number` int NOT NULL,
	`Policy_Details` varchar(100) NOT NULL,
	`Period` int NOT NULL,
	`Amount` float NOT NULL,
	`Premium` float NOT NULL,
	`Previous_Claims` float NOT NULL,
	`Premium_Paid` float NOT NULL,
	`Premium_Overdue` float NOT NULL,
	`Lock_In_Period` int NOT NULL,
	PRIMARY KEY (`Case_Number`)
);