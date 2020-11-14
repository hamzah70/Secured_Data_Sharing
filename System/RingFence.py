# Secured Data Movement
# Ring Fence

import json
import uuid
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa,padding

class rid:

    '''
        Record Identifier
            - Uniquely identifies a user record
            - Loads the relevant policy
            - Segregate attributes according to policy into segments
            - Generates key pairs for different segments
    '''

    __uniqueID = None
    __policy = None
    __privateKey = {}           
    __publicKey = {}
    __shared_data = {}
    __confidential_data = []      

    def __init__(self, policy_document):

        self.uniqueID = __gen_ID()

        with open(policy_document,"r") as file:
            self.__policy = json.load(file)

        file.close()

        __update()

    def __gen_ID(self):
        # Generates a unique identifier and append it to the record of generated identifiers.
        
        RID = set()
        
        with open("RID.txt","r") as file:
            data = file.readlines()
            for i in data : 
                RID.append(i)

        file.close()

        x = uuid.uuid1()
        while x in RID:
            x = uuid.uuid1()

        RID.add(x)

        with open("RID.txt","a") as file:
            file.write(str(x)+"\n")

        file.close()

        self.__uniqueID = x

    def __update():
        # Resolves shareable data and generate keys

        for ring in self.__policy:
            self.__shared_data[ring] = []
            for attribute in self.__policy[ring]:
                if ring[attribute] == 1:
                    self.__shared_data[ring].append(attribute)
                else:
                    self.__confidential_data.append(attribute)

        public, private = self.__generateKeys()

        self.public_key["Secret"] = public
        self.private_key["Secret"] = None

        for ring in self.__shared_data:
            public, private = self.__generateKeys()
            self.public_key[ring] = public
            self.private_key[ring] = private

    def setPolicy(self, custom_policy):
        with open(custom_policy,"r") as file:
            self.__policy = json.load(file)
        __update()

    def getPolicy(self):
        return self.__policy

    def getID(self):
        return self.__uniqueID

    def getSharedData(self):
        return self.__shared_data

    def getPublicKey(self):
        return self.__publicKey

    def __generateKeys(self):
        private_key = rsa.generate_private_key( public_exponent=65537, key_size=2048, backend=default_backend())
        public_key = private_key.public_key()
        return public_key, private_key


class ring_fence:

    '''
        Ring Fenced Data Block
            - Accesses data using RID
            - Creates the ring fences and enforces encryption
            - Dissolves the ring fences
            - Returns Extracted Data
    '''

    __RID = None
    Data_Block = {}

    def __init__(self, rid):
        self.__RID = rid

    def create(self, *args):
<<<<<<< HEAD
        # Creates the ring fence based on policy agreement.

        for ring in self.__RID.__shared_data:
            self.Data_Block[i] = {} 

        for label, data in args:
            for ring in self.__RID.getSharedData():
                if label in self.__RID.getSharedData()[ring]:
=======
        for ring in self.__RID.getPolicy()["Health_Records"].keys():
            self.Data_Block[i] = {} 

        for label, data in args:
            for ring in self.__RID.getPolicy()["Health_Records"].keys():
                if label in self.__RID.getPolicy()["Health_Records"][ring]:
>>>>>>> 7f87413339200e3061cf181c79c8c66f0d5262c5
                    key = self.__RID.getPublicKey()[ring]
                    encryptedData = encryptData(data,key)
                    Data_Block[ring][label] = encryptData
                else:
                    Data_Block[ring][label] = None

        Data_Block["MetaData"] = {}
        Data_Block["MetaData"]["RID"] = self.__RID.getID()
        Data_Block["MetaData"]["Policy"] = self.__RID.getPolicy()

        return Data_Block

    def dissolve(self, keys):
        # Dissolves the ring fence based on policy agreement.

        Decrypted_Data = {}

        for ring in self.Data_Block.keys():
            key = keys[ring]
            for k, v in self.Data_Block[ring].items():
                if v!=None:
                    decryptedData = decryptData(v,key)
                    Decrypted_Data[k] = decryptedData

        return Decrypted_Data


    def encryptData(self, data, key):
        encryptedData = key.encrypt(
                    message,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                        )
                    )
        return encryptedData

    def decryptData(self, data, key):
        decryptedData = key.decrypt(
                    encrypted,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                        )
                    )
        return decryptedData


<<<<<<< HEAD

=======
class rid:

    __uniqueID = None
    __policy = None
    __privateKey = {}			
    __publicKey = {}
    __shared_data = {}
    __confidential_data = []
    __dataAccess = {}  		

    def __init__(self, policy):
        for d in (policy["Health_Records"]["Medical_Records_1"], policy["Health_Records"]["Medical_Records_2"], 
            policy["Health_Records"]["Medical_Records_3"], policy["Health_Records"]["Addictions"]): self.__dataAccess.update(d)
        self.uniqueID = __gen_ID()
        self.__policy = policy
        __update()


    def __gen_ID(self):
    	RID = set()
		with open("RID.txt","r") as file:
		data = file.readlines()
		for i in data : 
			RID.append(i)

		file.close()

		x = uuid.uuid1()
		while x in RID:
			x = uuid.uuid1()

		RID.add(x)

		with open("RID.txt","w") as file:
			for i in RID:
				file.write(i+"\n")

		file.close()

		return x


    def __update():
        for i, k in enumerate(policy["Health_Records"].keys()):
            encrypt = 0
            for key, value in policy["Health_Records"][k].items():
                if value==1:
                    encrypt = 1
                    break
            if encrypt:
                self.__shared_data.append(k)

        public, private = self.__generateKeys()

        self.public_key[-1] = public
        self.private_key[-1] = 0

        for ring in self.__shared_data:
            public, private = self.__generateKeys()
            self.public_key[ring] = public
            self.private_key[ring] = private

    def setPolicy(self, custom_policy ):
        self.__policy = custom_policy
        for d in (policy["Health_Records"]["Medical_Records_1"], policy["Health_Records"]["Medical_Records_2"], 
            policy["Health_Records"]["Medical_Records_3"], policy["Health_Records"]["Addictions"]): self.__dataAccess.update(d)
        __update()

    def getPolicy(self):
        return self.__policy

    def getPublicKey(self):
        return self.__publicKey

    def __generateKeys(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return public_key, private_key
>>>>>>> 7f87413339200e3061cf181c79c8c66f0d5262c5
