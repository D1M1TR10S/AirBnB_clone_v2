#!/usr/bin/python3
'''
   Generates a tgz archive for web_static deployment
'''
from fabric.api import *
import tarfile
import os
import errno
from time import strftime


def do_pack():
    '''
        Creates directory and packs web_static folder into a .tgx archive
    '''
    dt = strftime("%Y%m%d%H%M%S")
    archive = "web_static_{}.tgz".format(dt)
    try:
        local("mkdir -p versions")
        local("tar -cfzv versions/{} web_static".format(archive))
    except:
        return None

    print("Packing web_static to " + archive) 
    size = os.stat(archive).st_size
    print('web_static packed: {} -> {}Bytes'.format(path, size))

    return ("versions/" + archive)
