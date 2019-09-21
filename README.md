HETS API [![Build Status](https://travis-ci.com/gibso/hets-api.svg?branch=master)](https://travis-ci.com/gibso/hets-api)
=================================

This project is part of the [Orpheus Application](https://github.com/gibso/orpheus-dev)

The [Orpheus Project](https://github.com/gibso/orpheus) implements a computational framework for conceptual blending with mental spaces extracted from the [ConceptNet knowledge base](https://github.com/commonsense/conceptnet5).

### Overview
This is a flask service, that serves as a API-Extension for the [The Heterogeneous Tool Set (HETS)](https://github.com/spechub/Hets).
It has currently two endpoints that accept a .casl file, and perform a translation into .th or .xml files.

### Endpoints

when running the server e.g. on http://localhost:5000, you can request the following endpoints:
* ##### POST  http://localhost:5000/generator/th
* ##### POST  http://localhost:5000/generator/xml

the endpoints expect a .casl file in your request. Make sure to place it as a `multipart/form-data` object under a key called `file`. If you have trouble with that, take a look at the [test file](https://github.com/gibso/hets-api/blob/master/tests/generator_test.py).

### Setup

clone this project by running 
```
git clone git@github.com:gibso/hets-api.git
```

and enter the directory: `cd hets-api`

#### Setup Using [docker](https://www.docker.com/get-started)
Build a docker image of the project by running
```
docker build -t hets-api .
```

Then you can start the flask server in a docker container by running
```
docker run --rm -it -p 5000:5000 hets-api
```
Now you can reach your server at http://localhost:5000 


#### Setup without docker
Python3 and virtualenv is required. After you created a virtual python environment for the project you can install the project requirements with 
```
pip install -e . 
```
Then you can start the flask server by running
```
flask run
```
Now you can reach your server at http://localhost:5000 

### to be considered
Currently the files are created in the  `/opt/data/` location. However, this is only useful when running the project in a docker container, then you can mount any local folder to the containers `/opt/data` location:
```
docker run --rm -it -p 5000:5000 -v ~/data:/opt/data hets-api
```

## Author

Developed by Oliver Görtz.

Contact me via [GitHub](https://github.com/gibso), [XING](https://www.xing.com/profile/Oliver_Goertz9), [Facebook](https://www.facebook.com/ogoertz), [Twitter](https://twitter.com/SuperMcOli) or just write an [email](mailto:oliver.goertz@gmail.com).
