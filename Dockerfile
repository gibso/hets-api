FROM spechub2/hets:latest

# install virtual env
RUN apt-get update
RUN apt-get install -y python3-pip

# add workdir for project
RUN mkdir /opt/project
WORKDIR /opt/project

# create virtual python env
#RUN python3 -m venv venv

# copy setup file
COPY setup.py .

# activate python env and install dependencies
RUN  pip3 install -e .

# start flask server
CMD flask run --host=0.0.0.0
