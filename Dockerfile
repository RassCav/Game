FROM alpine:3.5

RUN apk add --update py2-pip

COPY requirements.txt /tmp/requirements.txt

RUN python3 -m pip install -r /tmp/requirements.txt

EXPOSE 5000

CMD ["python", "dices.py"]