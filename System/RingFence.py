# Secured Data Movement
# Ring Fence

import uuid
import json
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa,padding

class rid:

    '''
        Record Identifier
            - Uniquely identifies a user record
            - Loads the relevant policy
            - Segregate attributes into segments, according to the policy 
            - Generates cryptographic keys for different segments
    '''

    __uniqueID = None
    __policy = None
    __Key = {}
    __shared_data = {}
    __confidential_data = []      

    def __init__(self, policy_document):

        self.__uniqueID = self.__gen_ID()

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

        key = self.__generateKeys()

        for ring in self.__shared_data:
            key = self.__generateKeys()
            self.__Key[ring] = key
            
    def setPolicy(self, custom_policy):
        with open(policy_document) as file:
            self.__policy = json.load(file)
        self.__update()

    def getPolicy(self):
        return self.__policy

    def getID(self):
        return self.__uniqueID

    def getSharedData(self):
        return self.__shared_data

    def getKey(self):
        return self.__Key

    def __generateKeys(self):
        key = Fernet(Fernet.generate_key())
        return key


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

        confidential = []
        temp_key = Fernet(Fernet.generate_key())

        for label, data in args:
            for ring in self.__RID.getSharedData():
                if label in self.__RID.getSharedData()[ring]:
                    key = self.__RID.getKey()[ring]
                    encryptedData = encryptData(data,key)
                    Data_Block[ring][label] = encryptData
                else:
                    confidential.append(data)

        data = encryptData(confidential,temp_key)

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
        data = str([data]).encode()
        encryptedData = key.encrypt(data)
        return encryptedData

    def decryptData(self, data, key):
        decryptedData = key.decrypt(data)
        data = eval(decryptedData.decode())[0]
        return data