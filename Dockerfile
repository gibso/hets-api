FROM spechub2/hets:latest

RUN apt-get update
RUN apt-get install -y python3-pip

RUN /usr/bin/pip3 install Flask

# add workdir for mounting the project
RUN mkdir /opt/project
WORKDIR /opt/project

CMD flask run --host=0.0.0.0

