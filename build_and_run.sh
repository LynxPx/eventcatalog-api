#!/bin/bash

# Build the Docker image
docker build -t eventcatalog-api .  

# Run the container
docker run -p 8000:80 eventcatalog-api
