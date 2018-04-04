#!/usr/bin/python3
'''
   Generates a tgz archive for web_static deployment
'''
from fabric.api import local
from time import strftime
import os


def do_pack():
    '''
        Creates an archive & packs it with the web_static folder
    '''
    dt = strftime("%Y%m%d%H%M%S")
    archive = "versions/web_static_{}.tgz".format(dt)
    local("mkdir -p versions")
    try:
        local('tar -cvzf {} web_static'.format(archive))
        return archive
    except:
        return None
