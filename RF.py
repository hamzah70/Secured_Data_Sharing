
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from temp import column_sets

class ring_fence:

    self.__RID = None
    self.Data_Block = {}

    def __init__(self, rid):
        self.__RID = rid

    def create(self, *args):

        for ring in self.__RID.getPolicy():
            self.Data_Block[i] = [] 

        for label, data in args:
            for ring in self.__RID.getPolicy():

                if label in self.__RID.getPolicy()[ring]:

                    key = self.__RID.getPublicKey()[ring]
                    Data_Block[ring].append(encryptData(data,key))

        return Data_Block

    def break_(self,keys):
        Decrypted_Data = []

        for ring in self.Data_Block:
            for data in self.Data_Block[ring]:

                key = keys[ring]
                Decrypted_Data.append(decryptData(data,key))

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


class rid:

    __uniqueID = None
    __policy = None
    __privateKey = {}			
    __publicKey = {}
    __shared_data = {}
    __confidential_data = []  		

    def __init__(self, policy):

        self.uniqueID = id(self)
        self.__policy = policy
        __update()

    def __update():

        for attribute in self.__policy:
            if attribute[1] == -1:
                self.__confidential_data.append(attribute[0])

            else:
                if attribute[1] in self.__shared_data:
                    self.__shared_data[attribute[1]].append(attribute[0])
                else:
                    self.__shared_data[attribute[1]] = [attribute[0]]

        public, private = self.__generateKeys()

        self.public_key[-1] = public
        self.private_key[-1] = 0

        for ring in self.__shared_data:
            public, private = self.__generateKeys()
            self.public_key[ring] = public
            self.private_key[ring] = private

    def setPolicy(self, custom_policy ):

        self.__policy = custom_policy
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
