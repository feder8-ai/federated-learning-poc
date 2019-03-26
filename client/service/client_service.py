from client.operations_utils.functions import get_deserialized_public_key
from client.service.model_service import ModelFactory
from client.service.server_service import ServerService

TRAINED_MODELS = {}


class Client:

    def __init__(self, config, X, y):
        self.client_id, self.client_name = config['CLIENT_ID'], config['NAME']
        self.client_ip = config['IP']
        self.client_port = config['PORT']
        self.config = config
        self.X, self.y = X, y
        self.model = None

    def process(self, model_type, encrypted_model):
        self.model = self.model if self.model else ModelFactory.get_model(model_type)
        training_model = self.model(self.client_name, self.X, self.y, self.pubkey)
        gradient = training_model.process(encrypted_model)
        TRAINED_MODELS[self.client_id] = training_model
        return gradient

    def register(self):
        response = ServerService(self.config).register(self.get_register_data())
        self.pubkey = get_deserialized_public_key(response['pub_key'])

    def get_register_data(self):
        return {'id': self.client_id,
                'ip': self.client_ip,
                'port': self.client_port
                }

    def make_step(self, encrypted_model):
        TRAINED_MODELS[self.client_id].gradient_step(encrypted_model)        

class ClientFactory:

    @classmethod
    def create_client(cls, name, X, y):
        return Client(name, X, y)