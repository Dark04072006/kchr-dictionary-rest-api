#! /bin/bash

source .venv/bin/activate

alembic -c conf/alembic.ini upgrade head
uvicorn app.main.web_api:create_app --factory --lifespan on
