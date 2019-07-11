FROM spechub2/hets:latest

# install pip
RUN apt-get update
RUN apt-get install -y python3-pip

# copy requirements file and install python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# add workdir for mounting the project
RUN mkdir /opt/project
WORKDIR /opt/project

# start flask server
CMD flask run --host=0.0.0.0

