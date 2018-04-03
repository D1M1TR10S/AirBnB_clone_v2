#!/usr/bin/env bash
# Sets up a static web page onto a server

# Updates, installs, and starts nginx
sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start

# Makes directories for static content
sudo mkdir -p /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/

# Creates an index file
sudo echo "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html

# Makes '/data/web-static/current' file a symbolic link to /test/ folder
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Sets ownership of /data/ and all subdirectories to ubuntu and vagrant
sudo chown -R ubuntu:vagrant /data/ .[^.]*

# Updates Nginx config to serve content of /data/web_static/current/ to hbnb_static
sudo sed -i "37i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}" /etc/nginx/sites-enabled/default

# Restarts nginx to apply changes
sudo service nginx restart
