# Use the Ubuntu 22.04 LTS image as the base image
FROM ubuntu-latest

# Install the Python runtime
RUN apt-get update && apt-get install -y python3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a non-root user and switch to it
RUN useradd -m appuser
USER appuser

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app/
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django application
CMD ["python", "src/PetsFinder/manage.py", "runserver", "0.0.0.0:8000"]
