import requests
import logging


class FederatedTrainerConnector:

    def __init__(self, config):
        self.federated_trainer_host = config['FEDERATED_TRAINER_HOST']

    def register(self, client_data):
        """
        Register client on federated server
        :param client_data:
        :return:
        """
        server_register_url = self.federated_trainer_host + "/dataowner"
        logging.info("Register client {} to server {}".format(client_data, server_register_url))
        response = requests.post(server_register_url, json=client_data)
        response.raise_for_status()
        #print(response)
        return response.json()
