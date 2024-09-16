# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the backend code to the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port (5001)
EXPOSE 5001

# Command to run the backend Flask app
CMD ["python", "app.py"]

