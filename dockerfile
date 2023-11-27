FROM python:3.8

ENV PYTHONBUFFERED=1
WORKDIR /app
COPY . /app/

RUN pip install --no-cache-dir nitter-miner

CMD ["nitter", "-q", "'leagueoflegends OR lol'", '-p', '10']
