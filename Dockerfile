# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install required packages
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application files
COPY . .

# Expose port for the app
EXPOSE 5002

# Command to run the app
CMD ["python", "app.py"]

