#!/bin/bash

docker login -u $DOCKER_LOGIN_USR -p $DOCKER_LOGIN_PSW

docker-compose build --parallel
