# Cars API

Simple REST API - basic cars make and model database interacting with https://vpic.nhtsa.dot.gov/api API


try it on heroku:
http://cars-django-api.herokuapp.com/

### Dependencies

* Django Rest Framework
* Docker

### Installing
you need docker to run it localy
* clone respository
* RUN: docker build -t cars_api -f Dockerfile-local .

### Executing program

* docker run -it -p 8000:8000 cars_api

You can now add and rate cars :D

HEROKU HOST: http://cars-django-api.herokuapp.com <br />
LOCAL HOST: http://localhost:8000/

### AVAILABLE endpoints:

#### POST /cars/

example json body:<br />
{ <br />
    "make": "",    #car make ex ford<br />
    "model": ""    \#car model ex mustang<br />
}

#### POST /rating/

example json body:<br />
{<br />
    "car": 7,    \#car PK<br />
    "rate": 2    \#rate int 1-5<br />
}

#### GET /cars/

shows the list of cars in databese

#### GET /popular/

shows top rated cars
