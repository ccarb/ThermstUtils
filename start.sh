#!/bin/bash
app="flask_estimulador"
docker build -t ${app}:latest .
docker run --privileged -p 5000:5000 ${app}:latest