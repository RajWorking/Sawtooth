FROM ubuntu:20.04

ADD transaction_family.py .
ADD transaction_processor.py .
ADD requirements.txt .

RUN apt-get update && apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt

# CMD python3 transaction_processor.py

STOPSIGNAL SIGTERM
