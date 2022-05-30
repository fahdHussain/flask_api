#!/bin/bash
export FLASK_APP=./main/index.py
. $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0
