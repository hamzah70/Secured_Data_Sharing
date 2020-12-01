# Secured Data Movement
# Ring Fence

import uuid
import json
import datetime
from cryptography.fernet import Fernet

class rid:

    __uniqueID = None
    __policy = None
    __key = {}
    __shared_data = {}
    __confidential_data = []      

    def __init__(self, policy_document):

        self.__uniqueID = self.__gen_ID()

        with open(policy_document) as file:
            self.__policy = json.load(file)
        file.close()

        self.__update()

    def __gen_ID(self):
        
        RID = set()
        
        with open("RID.txt","r") as file:
            data = file.readlines()
            for i in data : 
                RID.add(i)

        file.close()

        index = self.__policy["Details"]["Index"]

        x = uuid.uuid1(index)
        while x in RID:
            x = uuid.uuid1(index)

        RID.add(x)

        with open("RID.txt","a") as file:
            file.write(str(x)+"\n")

        file.close()

        return x

    def __update(self):

        for ring in self.__policy["Rules"]:
            self.__shared_data[ring] = []
            for attribute in self.__policy["Rules"][ring]:
                if self.__policy["Rules"][ring][attribute] == 1:
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

    __RID = None
    __Data_Block = {}

    def __init__(self, rid):
        self.__RID = rid

    def create(self, args):

        for ring in self.__RID.getSharedData():
            self.Data_Block[ring] = {} 

        confidential = []
        
        for label, data in args:
            for ring in self.__RID.getSharedData():

                if label in self.__RID.getSharedData()[ring]:
                    key = self.__RID.getKey()[ring]
                    encryptedData = encryptData(data,key)
                    Data_Block[ring][label] = encryptData
                else:
                    confidential.append(data)

        temp_key = Fernet(Fernet.generate_key())
        masked = encryptData(confidential,temp_key)

        Data_Block["MetaData"] = {}
        Data_Block["MetaData"]["TimeStamp"] = datetime.now()
        Data_Block["MetaData"]["RID"] = self.__RID.getID()
        Data_Block["MetaData"]["Policy"] = self.__RID.getPolicy()["Details"]

        return Data_Block

    def dissolve(self, keys):

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