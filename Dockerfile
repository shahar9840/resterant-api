FROM amd64/python:3.10-slim

WORKDIR /Resterant_API

RUN pip install Flask Flask-RESTful Flask-SQLAlchemy Flask-Cors psycopg2-binary

COPY . .

CMD python server.py

