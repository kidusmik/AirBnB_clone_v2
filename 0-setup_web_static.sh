#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

sudo apt-get -y upgrade
sudo apt-get -y update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
printf "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

printf %s "server {
	listen 80;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	add_header X-Served-By $hostname;
	location /hbnb_static {
		alias /data/web_static/current;
		index 103-index.html;
	}
	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	error_page 404 /custom_404.html;
}" > /etc/nginx/sites-available/default

service nginx reload
