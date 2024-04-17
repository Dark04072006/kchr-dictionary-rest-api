#! /bin/bash

source .venv/bin/activate

alembic -c conf/alembic.ini upgrade head
gunicorn -c conf/gunicorn.conf.py 'app.main.web_api:create_app()'
