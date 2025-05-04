FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install git (required for installing packages via git+ssh)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy your application code
COPY . /app

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 5000

# Command to run the FastAPI app
CMD ["python3", "app.py"]
