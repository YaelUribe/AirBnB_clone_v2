#!/usr/bin/env bash
# 
sudo su
apt-get update && apt-get -y upgrade
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "<html>
    <head></head>
    <body>OEEEEEEE</body>
</html>" > /data/web_static/releases/test/index.html
ln -s /data/web_static/releases/test/index.html /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '25i location /hbnb_static {\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service restart nginx
