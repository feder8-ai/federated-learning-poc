class EncryptionService:

    def __init__(self, homomorphic_encryption):
        self.homomorphic_encryption = homomorphic_encryption
        self.public_key = None

    def set_public_key(self, public_key):
        self.public_key = public_key

    def encrypt_collection(self, collection):
        return self.homomorphic_encryption.encrypt_vector(collection)

    def get_serialized_encrypted_value(self, value):
        return self.homomorphic_encryption.get_serialized_encrypted_value(value)

    def get_serializated_collection(self, collection):
        return [self.get_serialized_encrypted_value(value) for value in self.encrypt_collection(collection)]
