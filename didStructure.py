
# DID Document

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from temp import column_sets

class did:

	# Private data members
	__privateKey = {}			
	__publicKey = {}  		
	__algorithm = {}
	__dataAccess = []
	__policy = []		

	def __init__(self, *args, algorithm, custom_policy):
		""" args contain a tuple from the hospital database as 
		variable. All those attributes that are required by the 
		insurance data have their corresponding variable 
		names values as 1 and those tuples which the insurance 
		company does not have access to have the corresponding 
		variable name value as 0 in the policy. """

		self.__dataAccess = args
		self.__algorithm = algorithm
		__updatePolicy(custom_policy)

		for i in range(len(self.__policy)):
			public, private = self.__generateKeys()
			if policy[i]:
				self.__publicKey.append(public)
				self.__privateKey.append(private)
			else:
				self.__privateKey.append("gibberish")
				self.__publicKey.append("gibberish")

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
		for i in range(len(self.__dataAccess)):
			if custom_policy[i]:
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
