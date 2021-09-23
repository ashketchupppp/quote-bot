FROM python:3.9-buster
ARG TOKEN
ARG MONGO_CONN_STR

COPY . /discord-bot

RUN pip3 install -r /discord-bot/requirements.txt
RUN echo "TOKEN=${TOKEN}" > /discord-bot/.env
RUN echo "MONGO_CONN_STR=${MONGO_CONN_STR}" >> /discord-bot/.env

ENTRYPOINT ["python", "/discord-bot/src/bot.py"]
