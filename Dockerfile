# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the service account key file into the container
COPY mytextgeneratorapp-3594be0c38df.json /app/credentials.json

# Set the environment variable to use the credentials for Google Cloud
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/credentials.json"

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
