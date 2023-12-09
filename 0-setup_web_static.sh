#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static
if ! command -v nginx &> /dev/null
then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
printf " <html>
     <head>
     <\head>
     <body>
       Holberton School
     <\body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

config_content=$(cat <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
	return 301 \$scheme://youtube.com/watch?v=QH2-TGUlwu4\$request_uri;
    }
   
    error_page 404 /404.html;
    location = /404.html{
       internal;
    }
}
EOF
)

# Check if the alias already exists in the Nginx config
if ! grep -q "location /hbnb_static/" /etc/nginx/sites-available/default
then
	echo "$config_content" | sudo tee /etc/nginx/sitessystemctl status nginx.service-available/default > /dev/null
fi

#restart ngix
sudo service nginx restart

exit 0