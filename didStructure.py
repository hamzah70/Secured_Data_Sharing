from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class didStructure:
	# Private data members
	__privateKey = None			
	__dataAccess = []			
	__publicKey = None  		
	__algorithm = None

	def __init__(self, *args, algorithm):
		""" args contain a list of all the tuples from the hospital 
		database as variables. All those tuples that are required 
		by the insurance data have their corresponding variable 
		names values as 1 and those tuples which the insurance 
		company does not have access to have the corresponding 
		variable name value as 0 """

		self.__dataAccess = args
		self.__algorithm = algorithm
		self.publicKey, self.__privateKey = self.__generateKeys()
		self.uniqueID = id(self)

	def __generateKeys(self):
		private_key = rsa.generate_private_key(
			public_exponent=65537,
			key_size=2048,
			backend=default_backend()
		)
		public_key = private_key.public_key()
		return public_key, private_key

	def setDataAccess(self, **kwargs):
		self.__dataAccess = kwargs

	def getDataAccess(self):
		return self.__dataAccess

	def getPublicKey(self):
		return self.__publicKey

	def decryptData(self, data):
		decryptedData = self.__privateKey.decrypt(
								encrypted,
								padding.OAEP(
									mgf=padding.MGF1(algorithm=hashes.SHA256()),
									algorithm=hashes.SHA256(),
									label=None
								)
							)
		return decryptedData

	def encryptData(self, data):
		encryptedData = self.__publicKey.encrypt(
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



