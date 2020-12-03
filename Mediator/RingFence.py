# Secured Data Movement
# Ring Fence

import uuid
import json
import datetime
from cryptography.fernet import Fernet


class rid:

    __uniqueID = None
    __policy = None
    __keys = None
    __shared = None
    __masked = None  

    def __init__(self, policy_document):

        self.__shared = {}
        self.__masked = []
        self.__keys = {}

        with open(policy_document) as file:
            self.__policy = json.load(file)
        file.close()

        self.__uniqueID = self.__gen_ID()
        self.__update()

        self.__shared = str(self.__shared)
        self.__masked = str(self.__masked)
        self.__keys = str(self.__keys)

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
            self.__shared[ring] = []

            for attribute in self.__policy["Rules"][ring]:

                if self.__policy["Rules"][ring][attribute] == 1:
                    self.__shared[ring].append(attribute)
                else:
                    self.__masked.append(attribute)

        for ring in self.__shared:
            key = self.__generateKeys()
            self.__keys[ring] = key
            
    def setPolicy(self, custom_policy):
        with open(policy_document) as file:
            self.__policy = json.load(file)
        self.__update()

    def getPolicy(self):
        return self.__policy

    def getID(self):
        return self.__uniqueID

    def getShared(self):
        return self.__shared

    def getKeys(self):
        return self.__keys

    def __generateKeys(self):
        key = Fernet.generate_key()
        return key

class ring_fence:

    __RID = None
    __Data_Block = {}

    def __init__(self, rid):
        self.__RID = rid

    def create(self, args):

        Shared = eval(self.__RID.getShared())
        Keys = eval(self.__RID.getKeys())
        Confidential = []

        for ring in Shared:
            self.__Data_Block[ring] = {} 

        for label in args:
            
            for ring in Shared:
                
                if label in Shared[ring]:

                    key = Fernet(Keys[ring])
                    encryptedData = self.encryptData(args[label],key)
                    self.__Data_Block[ring][label] = encryptedData
                
                else:

                    Confidential.append(args[label])

        temp_key = Fernet(Fernet.generate_key())
        masked = self.encryptData(Confidential,temp_key)

        self.__Data_Block["MetaData"] = {}
        self.__Data_Block["MetaData"]["TimeStamp"] = datetime.datetime.now()
        self.__Data_Block["MetaData"]["RID"] = self.__RID.getID()
        self.__Data_Block["MetaData"]["Policy"] = self.__RID.getPolicy()["Details"]

    def getBlock(self):
        return self.__Data_Block

    def dissolve(self, keys):

        Decrypted_Data = {}
        keys = eval(keys)

        for ring in self.__Data_Block:

            if ring != "MetaData":
                key = Fernet(keys[ring])

                for label in self.__Data_Block[ring]:
                    value = self.__Data_Block[ring][label]
                    Decrypted_Data[label] = self.decryptData(value,key)
            else:
                Decrypted_Data[ring]=self.__Data_Block[ring]

        return Decrypted_Data

    def encryptData(self, data, key):
        data = str([data]).encode()
        encryptedData = key.encrypt(data)
        return encryptedData

    def decryptData(self, data, key):
        decryptedData = key.decrypt(data)
        data = eval(decryptedData.decode())[0]
        return data
