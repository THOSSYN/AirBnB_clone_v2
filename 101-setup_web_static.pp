# A puppet manifest to create a web root directory

$config = '<html>
   <head>
   </head>
   <body>
     Holberton School
   </body>
 </html>',

exec { 'install_and_configure':
  command  => 'sudo apt-get update &&
	       sudo apt-get install nginx -y &&
	       sudo mkdir /data/web_static/releases/test/ &&
	       sudo mkdir /data/web_static/shared/ &&
	       sudo echo $config > /data/web_static/releases/test/index.html &&
	       sudo ln -sf /data/web_static/releases/test/ /data/web_static/current &&
	       sudo chown -R ubuntu:ubuntu /data/ &&
	       update="\\\n\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}" &&
	       sudo sed -i "55i $update" /etc/nginx/sites-available/default &&
	       sudo service nginx restart',
  provider =>  'shell',
}
