#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

location="        location \/hbnb_static/ { alias /data/web_static/current/; }"

sudo apt-get update
sudo apt-get -y install nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "$content" | sudo tee /data/web_static/releases/test/index.html
ln -sfn /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data

sudo sed -i "55 i\ $location" /etc/nginx/sites-available/default
# restart nginx
sudo service nginx start