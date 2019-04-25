import logging
import os
from logging.config import dictConfig
from flask import Flask, request, jsonify
from client.data.data_loader import DataLoader
from client.exceptions.exceptions import InvalidModelException
from client.service.client_service import ClientFactory
from client.service.model_service import ModelType
from commons.decorators.decorators import serialize_encrypted_data, deserialize_encrypted_data
from commons.encryption.encryption_service import EncryptionService

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


def create_app():
    # create and configure the app
    flask_app = Flask(__name__)
    # load the instance config
    flask_app.config.from_pyfile('config.py')
    # ensure the instance folder exists
    try:
        os.makedirs(flask_app.instance_path)
    except OSError:
        pass
    return flask_app



def build_data_loader(config):
    data_loader = DataLoader()
    data_loader.load_data(config['N_SEGMENTS'])
    return data_loader


def build_encryption_service(config):
    encryption_type = config['ENCRYPTION_TYPE']
    return EncryptionService(encryption_type())


# Global variables
app = create_app()
data_loader = build_data_loader(app.config)
encryption_service = build_encryption_service(app.config)
client = ClientFactory.create_client(app.config, data_loader, encryption_service)


@app.errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args]
    status_code = error.status_code
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }
    return jsonify(response), status_code


@app.route('/weights', methods=['POST'])
@serialize_encrypted_data(encryption_service=encryption_service, schema=jsonify)
def process_weights():
    """
    process weights from server
    :return:
    """
    logging.info("Process weights")
    data = request.get_json()
    # Validate model type
    model_type = data['type']
    if not ModelType.validate(model_type):
        raise InvalidModelException(model_type)
    # encrypted_model
    return client.process(model_type, data["public_key"])


@app.route('/step', methods=['PUT'])
@deserialize_encrypted_data(encryption_service=encryption_service, request=request)
def gradient_step(data):
    """
    Execute step with gradient
    :return:
    """
    logging.info("Gradient step")
    client.step(data["gradient"])
    return jsonify(200)


@app.route('/model', methods=['GET'])
def get_model():
    logging.info("Get Model")
    return jsonify(client.get_model())


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(200)

