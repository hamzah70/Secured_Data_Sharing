
# DID Document

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from clustering import column_sets
from RF import *

class did:

	# Private data members
    __privateKey = {}
    __publicKey = {}
    __algorithm = {}
    __dataAccess = []
    __policy = []

    def __init__(self, algorithm, custom_policy):
        for d in (custom_policy["health_records"]["Medical_Records_1"], custom_policy["health_records"]["Medical_Records_2"], custom_policy["health_records"]["Medical_Records_3"], custom_policy["health_records"]["Addictions"]): self.__dataAccess.update(d)
        self.__algorithm = algorithm
        __updatePolicy(custom_policy)

        for i in range(len(self.__policy)):
            public, private = self.__generateKeys()
            if policy[i]:
                self.__publicKey.append(public)
                self.__privateKey.append(private)
            else:
                self.__privateKey.append("gibberish")
                self.__publicKey.append(public)

        __process()

        self.uniqueID = id(self)

    def __generateKeys(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return public_key, private_key

    def __updatePolicy(self, custom_policy):
        for i, k in enumerate(custom_policy["health_records"].keys()):
            encrypt = 0
            for key,value in custom_policy["health_records"][k].items():
                if value==1:
                    encrypt = 1
                    break
            if encrypt:
                self.__policy.append(1)
            else:
                self.__policy.append(0)

    def __process(self):
        for i in range(len(self.__dataAccess)):
            self.__dataAccess[i] = encryptData(self.__dataAccess[i],self.__privateKey[i])

    def setDataAccess(self, **kwargs):
        self.__dataAccess = kwargs

    def getDataAccess(self):
        return self.__dataAccess

    def getPublicKey(self):
        return self.__publicKey

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

    def executeCode(data):
        for i in range(len(data)):
            data[i] = decryptData(data[i])
