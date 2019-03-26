import numpy as np

from operations_utils.functions import get_encrypted_number, encrypt_vector, sum_encrypted_vectors, \
    get_serialized_gradient


class LinearRegression:
    """Runs linear regression with local data or by gradient steps,
    where gradient can be passed in.

    Using public key can encrypt locally computed gradients.
    """

    def __init__(self, name, weights, pubkey=None):
        self.name = name
        self.pubkey = pubkey
        self.weights = weights

    def predict(self, X):
        """Score test data"""
        return X.dot(self.weights)