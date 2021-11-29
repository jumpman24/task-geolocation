# Solution to Software Engineering League

## Install
To install requirements create and activate new virtual environment.
For example:
```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To run tests:
```shell
source venv/bin/activate
pytest
```

To run the server:
```shell
source venv/bin/activate
uvicorn app.main:app --host=0.0.0.0 --port=8000
```

You can see the OpenAPI documentation at http://0.0.0.0:8000/docs


Environment variables (app/config.py:Config):
```shell
DATABASE_URL - where is the database located
TOKEN - token to emulate admin authentication
ACCURACY - factor of coordinate approximation (in degrees)
```