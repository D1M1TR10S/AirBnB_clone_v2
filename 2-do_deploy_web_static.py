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

def do_pack():
    '''
        Creates an archive & packs it with the web_static folder
    '''
    dt = strftime("%Y%m%d%H%M%S")
    archive = "versions/web_static_{}.tgz".format(dt)
    if not os.path.isdir('versions'):
        os.makedirs('versions')
    try:
        local('sudo tar cvfz {} web_static'.format(archive))
        return archive
    except:
        return None

def do_deploy(archive_path):
    '''
        Deploys archive of web_static folder to webservers
    '''
    try:
        run("mkdir -p /tmp/")
        put(archive_path, "/tmp/")
        if archive_path.endswith(".tgz"):
            arch = archive_path[:-4]
        run("tar xvzf {} -C /data/web_static/releases/{}".format(archive_path, arch))
        run("rm -rf /tmp/{}".format(archive_path))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(arch))
        return True

    except:
        return False
