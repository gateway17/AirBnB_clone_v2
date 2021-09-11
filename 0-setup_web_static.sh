#!/usr/bin/env bash

path0 = /data/web_static/releases/test/
filename = /data/web_static/releases/test/index.html
to = /data/web_static/releases/test/
link = /data/web_static/current 

sudo apt-get install nginx
mkdir -r $path0
mkdir -r /data/web_static/shared/

if [ -d "$path0" ]; then
{
    sudo echo "JUST FOR TESTING" | sudo tee $filename
}

if [ ! -h $link ]; then
{
    rm -rf $link
    ln -fs $to $link
}

else 
{ 
    ln -s $to $link
}

chown -R /data/ ubuntu
sudo ln -fs 

