#!/bin/bash
if [[ -z "$1" || -z "$2" ]]; then
    echo "empty username $1 or tag $2"
    exit(1)
fi

echo "building nitter_miner:$2"
docker build -t nitter_miner .

# logs into docker
docker login


# tag and upload
docker tag nitter_miner "$1/nitter_miner:0.0.6"

# $1 expected to be version number
docker push "$1/nitter_miner:$2"

# docker run -it nitter_miner /bin/bash
