# Base Image
FROM python:3.7

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
#ENV PORT=8000

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv
RUN pip3 install dj-static
RUN pip3 install whitenoise
RUN pip3 install requests

# Install project dependencies
RUN pipenv install --skip-lock --system --dev

# Collect static files
RUN python manage.py collectstatic --noinput

# EXPOSE 8888
CMD gunicorn cars_api.wsgi:application --bind 0.0.0.0:$PORT
