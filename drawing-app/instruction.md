# Instruction

## Requirements

- Have `pipenv` installed 
- Python 3.9

Go to the `drawing-app` folder. 

Follow the below instructions to create the virtual environment,
install the code, and start the server. 

Run the following command to create the virtual environment under the current folder.
```
pipenv --python 3.9-dev install
pipenv shell
```

Install the package

```
pip install -e . 
```

Starts the server

```
python src/server/server.py
```

Run the unit tests

```
pytest
```