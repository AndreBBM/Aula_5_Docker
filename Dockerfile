# Use the official Python image as the base
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir flask==3.0.3 \
    Flask-HTTPAuth==4.8.0

# Expose the port the server is running on
EXPOSE 8080

# Create a volume for persistent storage of the database
VOLUME ["/app/src"]

# Move to the src folder
WORKDIR /app/src

# Run the database creation script and add users
RUN python3 adduser.py

# Run the server
CMD ["python3", "softdes.py"]