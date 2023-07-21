
FROM python:3.8-slim-buster
WORKDIR /recipe-subito
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD ["python3", "./main.py" ]