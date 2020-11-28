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

    uniqueID = None
    __policy = None
    __privateKey = {}           
    __publicKey = {}
    __shared_data = {}
    __confidential_data = []      

    def __init__(self, policy_document):

        self.uniqueID = self.__gen_ID()

        with open(policy_document) as file:
            self.__policy = json.load(file)

        file.close()

        self.__update()


    def __gen_ID(self):
        # Generates a unique identifier and append it to the record of generated identifiers.
        
        RID = set()
        
        with open("RID.txt","r") as file:
            data = file.readlines()
            for i in data : 
                RID.add(i)

        file.close()

        x = uuid.uuid1()
        while x in RID:
            x = uuid.uuid1()

        RID.add(x)

        with open("RID.txt","a") as file:
            file.write(str(x)+"\n")

        file.close()

        return x

    def __update(self):
        # Resolves shareable data and generate keys

        for ring in self.__policy:
            self.__shared_data[ring] = []
            for attribute in self.__policy[ring]:
                if self.__policy[ring][attribute] == 1:
                    self.__shared_data[ring].append(attribute)
                else:
                    self.__confidential_data.append(attribute)

        public, private = self.__generateKeys()

        self.__publicKey["Secret"] = public
        self.__privateKey["Secret"] = None

        for ring in self.__shared_data:
            public, private = self.__generateKeys()
            self.__publicKey[ring] = public
            self.__privateKey[ring] = private

    def setPolicy(self, custom_policy):
        with open(custom_policy,"r") as file:
            self.__policy = json.load(file)
        self.__update()

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

        # Creates the ring fence based on policy agreement.

        for ring in self.__RID.__shared_data:
            self.Data_Block[i] = {} 

        for label, data in args:
            for ring in self.__RID.getSharedData():
                if label in self.__RID.getSharedData()[ring]:
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
        
