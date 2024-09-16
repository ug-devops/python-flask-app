# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the frontend code to the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port (5000)
EXPOSE 5000

# Command to run the frontend Flask app
CMD ["python", "app.py"]

