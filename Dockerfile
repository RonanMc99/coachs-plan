# Get the latest base image
FROM python:3.8

# Environment vars
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip3 install pipenv && pipenv install --system

# Copy project
COPY . /code/
