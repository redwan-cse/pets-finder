
# Use an official Python runtime as a parent image
FROM python:3.12.0a1-alpine3.13

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
# ENV NAME SECRET_KEY

# Run app.py when the container launches
CMD ["python", "PetsFinder/manage.py", "runserver", "0.0.0.0:8000"]