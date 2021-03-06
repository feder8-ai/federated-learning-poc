# Federated learning - Data Owner


## Installing

A step by step series that tell you how to get a development env running

```
git clone git@github.com:DeltaML/federated-learning-poc.git
cd federated-learning-poc/
python3 -m venv venv
source venv/bin/activate
pip install -r data_owner/requirements.txt
```

## Run

### Using command line

``` bash
    gunicorn -b "0.0.0.0:8080" --chdir data_owner/ wsgi:app --preload
``` 


### Using Docker

Select _LOCAL_PORT_ number to run some containers
``` bash
    docker build -t federated-learning-data_owner --rm -f data_owner/Dockerfile .
    docker run --rm -it -p <LOCAL_PORT>:5000 federated-learning-data_owner
``` 


### Using Pycharm

	Script Path: .../data_owner/virtualenv/bin/gunicorn
	Parameters: -b "0.0.0.0:5000" wsgi:app --preload
	Working directory: ../data_owner


## Usage 
 
### Process weights

``` bash
curl -v -H "Content-Type: application/json" -X POST -d '{"type": "LINEAR_REGRESSION", "public_key": "XXXXXXXXXXXXXXXX"}' "http://localhost:5000/weights"
```

### Gradient step

``` bash
curl -v -H "Content-Type: application/json" -X POST -d '{"gradient":[{"w1":1}]}'  "http://localhost:9090/step"
```


### Get Model from data owner

``` bash
curl -v -H "Content-Type: application/json" -X GET "http://localhost:9090/model"
```



## Data Owner configuration

``` python3

N_SEGMENTS = 5
FEDERATED_TRAINER_HOST = "http://cte_federated_trainer:8080"
ETA = 1.5
REGISTRATION_ENABLE = True
ACTIVE_ENCRYPTION = False

```

### Configuration details

- N_SEGMENTS: __TODO__
- FEDERATED_TRAINER_HOST: __TODO__
- ETA: __TODO__
- REGISTRATION_ENABLE: __TODO__
- ACTIVE_ENCRYPTION: __TODO__
