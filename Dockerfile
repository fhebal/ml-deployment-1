# Base image
FROM python:3.9-slim-buster

LABEL maintainer="Ferdynand Hebal <ferdynandhebal@gmail.com>"
LABEL version="1.0"
LABEL description="A Docker image for serving a machine learning model."


# Set working directory
WORKDIR /app

# Copy contents of app directory
COPY app/ .
COPY models/model.joblib .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Define command to run when container starts
CMD ["python", "main.py"]
