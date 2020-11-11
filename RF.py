
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from clustering import column_sets

class ring_fence:

    __RID = None
    Data_Block = {}

    def __init__(self, rid):
        self.__RID = rid

    def create(self, *args):
        for ring in self.__RID.getPolicy()["health_records"].keys():
            self.Data_Block[i] = {} 

        for label, data in args:
            for ring in self.__RID.getPolicy()["health_records"].keys():
                if label in self.__RID.getPolicy()["health_records"][ring]:
                    key = self.__RID.getPublicKey()[ring]
                    encryptedData = encryptData(data,key)
                    Data_Block[ring][label] = encryptData
                else:
                    Data_Block[ring][label] = None

        return Data_Block

    def break_(self, keys):
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


class rid:

    __uniqueID = None
    __policy = None
    __privateKey = {}			
    __publicKey = {}
    __shared_data = {}
    __confidential_data = []
    __dataAccess = []  		

    def __init__(self, policy):
        for d in (policy["health_records"]["Medical_Records_1"], policy["health_records"]["Medical_Records_2"], 
            policy["health_records"]["Medical_Records_3"], policy["health_records"]["Addictions"]): self.__dataAccess.update(d)
        self.uniqueID = id(self)
        self.__policy = policy
        __update()

    def __update():
        for i, k in enumerate(policy["health_records"].keys()):
            encrypt = 0
            for key, value in policy["health_records"][k].items():
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
        for d in (policy["health_records"]["Medical_Records_1"], policy["health_records"]["Medical_Records_2"], 
            policy["health_records"]["Medical_Records_3"], policy["health_records"]["Addictions"]): self.__dataAccess.update(d)
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
