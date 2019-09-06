FROM spechub2/hets:latest

# install virtual env
RUN apt-get update
RUN apt-get install -y python3-pip

# add workdir for project
RUN mkdir /opt/project
WORKDIR /opt/project

# copy everything
COPY . .

# install dependencies
RUN  pip3 install -e .

# start flask server
CMD FLASK_APP=hets_api flask run --host=0.0.0.0
