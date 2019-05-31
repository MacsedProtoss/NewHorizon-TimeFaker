FROM python:alpine

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3","-u", "fake.py"]