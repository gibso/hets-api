FROM spechub2/hets:latest

# install virtual env
RUN apt-get update
RUN apt-get install -y python3-pip

# add workdir for project
RUN mkdir /opt/project
WORKDIR /opt/project

# copy everything
COPY . .

# activate python env and install dependencies
RUN  pip3 install -e .

# add directories for output files
RUN mkdir /data/th
RUN mkdir /data/xml

# start flask server
CMD flask run --host=0.0.0.0
