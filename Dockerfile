FROM python:3.11.9

WORKDIR /dictionary

COPY pyproject.toml /dictionary/pyproject.toml
COPY conf /dictionary/conf
COPY src /dictionary/src
COPY assets /dictionary/assets

RUN pip install -U pip
RUN pip install -e .
RUN cd /dictionary/
