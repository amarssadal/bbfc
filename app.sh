#!/usr/bin/env bash

export APP_CONFIG_FILE=prod.py
export FLASK_APP=app.py
flask db upgrade
python app.py