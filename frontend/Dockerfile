FROM python:3.8-slim-buster

RUN apt-get -y update

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .

CMD [ "python" , "run.py" ]
