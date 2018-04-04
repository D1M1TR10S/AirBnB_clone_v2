#!/usr/bin/python3
'''
    Packs an archive for web_static deployment
    Distributes it to both webservers, then unpacks
    the web static content
'''
from fabric.api import *
from time import strftime
import os


env.hosts = ['107.23.115.192', '34.228.158.73']

def do_deploy(archive_path):
    '''
        Deploys archive of web_static folder to webservers
    '''
    if not os.path.exists(archive_path):
        return False
    try:
        archive = archive_path[9:-4]
        put(archive_path, "/tmp/")
        new_path = "/tmp/{}.tgz".format(archive)
        run("mkdir -p /data/web_static/releases/{}/".format(archive))
        run("tar -xzf {} -C /data/web_static/releases/{}/".format(new_path, archive))
        run("rm /tmp/{}.tgz".format(archive))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(archive, archive))
        run("rm -rf /data/web_static/releases/{}/web_static/".format(archive))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive))
        return True

    except:
        return False
