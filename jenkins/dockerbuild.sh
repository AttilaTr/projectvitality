#!/bin/bash

curl https://get.docker.com | sudo bash

sudo usermod -aG docker jenkins

docker login -u $DOCKER_LOGIN_USR -p $DOCKER_LOGIN_PSW

version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

docker-compose up -d --build

docker exec vitality_server python create.py