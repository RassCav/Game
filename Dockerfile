FROM python:3.8-slim-buster
ADD . /python-flask
WORKDIR /python-flask
RUN PIP install -r requirements.txt
CMD ["python", "./dices.py"]