FROM python:2.7.15-alpine3.8

RUN pip install fake-useragent==0.1.10

ADD main.py /

CMD ["python", "/main.py"]