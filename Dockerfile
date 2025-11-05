# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the workdir
WORKDIR /app

# Install system dependencies 
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev musl-dev && \
    apt-get clean


# Copy requirements file and install dependencies.
COPY requirements.txt /app/


RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container

COPY . /app/

# Expose port 8000 for Django
EXPOSE 8000

# Run the Django Develeopment server
CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']



