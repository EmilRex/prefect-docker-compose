FROM prefecthq/prefect:3-latest

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U \
    prefect-docker
