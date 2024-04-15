#! /bin/bash

source .venv/bin/activate

gunicorn -c conf/gunicorn.conf.py 'app.main.web_api:create_app()'
