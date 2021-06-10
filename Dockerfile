# Start with barebones python 3.9 from alpine
FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY *.py .

CMD python3 p0.py output.css -i
