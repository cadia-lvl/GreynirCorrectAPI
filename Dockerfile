FROM pypy:3.7

RUN apt-get update && \
    apt-get install -y python3-dev

RUN mkdir /usr/src/app
COPY requirements.txt /usr/src/app/

RUN cd /usr/src/app \
 && pip install --upgrade pip \
 && pip install -r requirements.txt

WORKDIR /usr/src/app
COPY main.py main.py

EXPOSE 8080

ENTRYPOINT uvicorn main:app --port 8080 --host 0.0.0.0
