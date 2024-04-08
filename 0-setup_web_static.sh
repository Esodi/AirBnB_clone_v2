#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

sudo apt-get update -y -qq

sudo apt-get install nginx -y

sudo service nginx start

sudo mkdir -p /data/web_static/releases/

sudo mkdir -p /data/web_static/shared/

sudo mkdir -p /data/web_static/releases/test/

echo "SOME CONTENT" | sudo tee /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
	sudo rm /data/web_static/current
else
	sudo ln -s /data/web_static/current /data/web_static/releases/test/
fi

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i 's/\tserver_name _;/\tserver_name _;\n\n\tlocation \/hbnb_static\/{\n\t\talias \/data\/web_static\/current\/;\n\t\tindex /data/web_static/releases/test/index.html\n\t}/' /etc/nginx/sites-available/default

sudo service nginx restart
