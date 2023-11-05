#Pet-finder/src/Dockerfile
FROM python:3.12
WORKDIR /app
RUN apt update
RUN apt install -y default-libmysqld-dev
COPY . /app/
RUN pip install -r requirements.txt