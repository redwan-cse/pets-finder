## Pet Finder
This is the documentation for the Pet Finder Django application. 

## Installation
The latest Docker image is available on Docker Hub at `redwancse/pets-finder:latest`.

## Run the container
Use this command to run the image from remote host:
```shell
docker run -dp 0.0.0.0:8000:8000 redwancse/pets-finder:latest
```

## Run the container from localhost
Use this command to run the image from local host:
```shell
docker run -dp 127.0.0.1:8000:8000 redwancse/pets-finder:latest
```