from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class didStructure:
	__privateKey = None			# Private data member
	__dataAccess = {}			# Private data member
	__publicKey = None  		# Public data member

	def __init__(self, **kwargs):
		self.__dataAccess = kwargs
		self.publicKey, self.__privateKey = self.__generateKeys()

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
		original_message = self.__privateKey.decrypt(
								encrypted,
								padding.OAEP(
									mgf=padding.MGF1(algorithm=hashes.SHA256()),
									algorithm=hashes.SHA256(),
									label=None
								)
							)
	def encryptData(self, data):
		encrypted = self.__publicKey.encrypt(
						message,
						padding.OAEP(
							mgf=padding.MGF1(algorithm=hashes.SHA256()),
							algorithm=hashes.SHA256(),
							label=None
						)
					)

