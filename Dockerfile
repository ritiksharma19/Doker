# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Run pip to install any dependencies from requirements.txt
# Since we have no dependencies, no pip install is needed here

# Command to run the application
CMD ["python", "./library_app.py"]

