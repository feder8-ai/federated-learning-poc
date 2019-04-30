# Federated learning - Model Buyer

## Run

### Using command line
``` bash
    gunicorn -b "0.0.0.0:9090" --chdir model_buyer/ wsgi:app --preload
``` 


### Using Pycharm

	Script Path: .../model_buyer/virtualenv/bin/gunicorn
	Parameters: -b "0.0.0.0:9090" wsgi:app --preload
	Working directory: ../model_buyer


## Usage 
 
### Get model from federated trainer

``` bash
curl -v -H "Content-Type: application/json" -X POST "http://localhost:9090/model"
```

### Get prediction

``` bash
curl -v -H "Content-Type: application/json" -X GET "http://localhost:9090/predict"
```



## Model buyer configuration

``` python3

config = {
    'server_register_url': "http://localhost:8080/model",
    'key_length': 1024,
    'port': 9090,
    'active_encryption': False,
    'encryption_type': PheEncryption
}
```

### Configuration details

- server_register_url: __TODO__
- key_length: __TODO__
- port: __TODO__
- active_encryption: __TODO__
- encryption_type: __TODO__