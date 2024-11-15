# Use an official Python 3.9 image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
