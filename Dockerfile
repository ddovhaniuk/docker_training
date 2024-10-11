# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install the necessary Python packages
RUN pip install --no-cache-dir requests

# Define the command to run the script
CMD ["python", "./main.py"]
