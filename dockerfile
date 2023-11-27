FROM python:3.8

ENV PYTHONBUFFERED=1
WORKDIR /app
COPY . /app/

RUN pip install --no-cache-dir nitter-miner
RUN python -c "import nltk; nltk.download('all')"

# CMD ["~/.local/bin/nitter", "-q", "'leagueoflegends OR lol'", '-p', '10']
