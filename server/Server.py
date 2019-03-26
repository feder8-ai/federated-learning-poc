from model.linear_regression import LinearRegression
from operations_utils.functions import *
import requests
import phe as paillier
from service import ModelType

class Server:

    def __init__(self, key_length=20):
        self.clients = []
        self.keypair = paillier.generate_paillier_keypair(n_length=key_length)
        self.pubkey, self.privkey = self.keypair

    def sendGlobalModel(self, weights):
        """Encripta y envia el nombre del modelo a ser entrenado"""
        payload = {"encrypted_model": weights} 
        requests.put(client.ip + ":" + client.port + "/step", data = payload)

    def sendModelTypeToClient(client, model_type):
        requests.post(paillier.encrypt(model_type))

    def register_client(self, client):
        self.clients.append(client)

    def _getUpdateFromClient(client, model_type):
        return requests.post(client.ip + ":" + client.port + "/weights", data = {"type": model_type})

    def getUpdates(self, model_type):
        return [_getUpdateFromClient(client, model_type) for client in self.clients]

    def updateGlobalModel(self, updates):
        return server.decrypt_aggregate(sum(updates), len(self.clients))

    def chooseModel(self):
        return LinearRegressionModel

    def decrypt_aggregate(self, input_model, n_clients):
        return decrypt_vector(self.privkey, input_model) / n_clients

    def federated_learning(X_test, y_test, config):
        n_iter = config['n_iter']
        # Instantiate the server and generate private and public keys
        # NOTE: using smaller keys sizes wouldn't be cryptographically safe
        server = Server(key_length=config['key_length'])
        model = ModelFactory.get_model(model_type)
        n_clients = len(self.clients)

        # Instantiate the clients.
        # Each client gets the public key at creation and its own local dataset
        for client in self.clients:
            if not sendModelTypeToClient(client, model_type):
                raise RuntimeError

        # The federated learning with gradient descent
        print('Running distributed gradient aggregation for {:d} iterations'.format(n_iter))
        for i in range(n_iter):
            updates = getUpdates(model_type, model_type)
            updates = updateGlobalModel(updates)
            sendGlobalModel(client, updates)

        print('Error (MSE) that each client gets after running the protocol:')
        for i in len(self.clients):
            model = model(model_type, updates[i])
            y_pred = model.predict(X_test)
            mse = mean_square_error(y_pred, y_test)
            print('Client {:s}:\t{:.2f}'.format(i, mse))