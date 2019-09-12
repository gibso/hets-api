FROM ubuntu:18.04

# to avoid tzdata interaction
ARG DEBIAN_FRONTEND=noninteractive

# install dependencies
RUN apt-get update && \
    apt-get install -y \
    postgresql postgresql-server-dev-10 mysql-server \
    libmysqlclient-dev libglib2.0-dev libcairo2-dev \
    libpango1.0-dev libgtk2.0-dev libglade2-dev libncurses-dev

# install Haskell Tool Stack
RUN curl -sSL https://get.haskellstack.org/ | sh

WORKDIR /opt

# Get the HETS repository and its submodules
RUN git clone --recurse-submodules https://github.com/spechub/Hets.git

WORKDIR /opt/Hets

# Setup Stack for HETS
RUN stack setup
RUN make restack

# build HETS
RUN make

RUN apt-get update
RUN apt-get install -y python3-pip

# add workdir for project
RUN mkdir /opt/data
RUN mkdir /opt/project
WORKDIR /opt/project

# copy everything
COPY . .

# install dependencies
RUN  pip3 install -e .

# start flask server
CMD flask run --host=0.0.0.0
