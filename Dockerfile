FROM python:3.8.8-slim
WORKDIR /workspace

RUN apt-get update && apt-get install -y \
  apt-utils \
  dumb-init \
  git \
  ssh \
  htop \
  iftop \
  vim \
  libcurl4-openssl-dev \
  libssl-dev \
  python3-dev \
  gcc \
  build-essential \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY requirements.txt /workspace/requirements.txt
RUN pip install -r requirements.txt
COPY . /workspace
RUN pip install -e .

EXPOSE 5005
