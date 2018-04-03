#!/usr/bin/python3
'''
   Generates a tgz archive for web_static deployment
'''
from fabric.api import *
import tarfile
from time import strftime


def do_pack():
    '''
        Creates a directory and packs it with a .tgz archived  web_static folder
    '''
    dt = strftime("%Y%m%d%H%M%S")
    archive = "web_static_{}.tgz".format(dt)
    try:
        local("mkdir -p versions")
        local('tar -cvfz versions/{} web_static/'.format(archive))
        return "versions/{}".format(archive)
    except:
        return None
