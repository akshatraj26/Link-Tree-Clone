# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the workdir
WORKDIR /app

# Install system dependencies 
RUN apt-get update && apt-get install -y \
     gcc \
     python3-dev \
     default-libmysqlclient-dev \ 
     build-essential \
     pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Copy requirements file and install dependencies.
COPY requirements.txt /app/


RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt 

# Copy project files into the container

COPY . /app/

# Expose port 8000 for Django
EXPOSE 8000

# Run the Django Develeopment server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



