#! /bin/bash

source .venv/bin/activate

uvicorn app.main.web_api:create_app --factory --lifespan on
