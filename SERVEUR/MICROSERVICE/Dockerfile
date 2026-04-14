FROM python:3.14-slim

WORKDIR /Multiservice-python

COPY SERVEUR/MICROSERVICE/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY SERVEUR/MICROSERVICE/ .

CMD [ "python","serveur.py" ]