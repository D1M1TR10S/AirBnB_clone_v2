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
    directory = os.path.dirname("versions")
    dt = strftime("%y\%m\%d\%h\%m\%s")
    archive = "web_static_{}.tgz".format(dt)
    try:
        os.makedirs(directory)
        tar = local("tar -cfzv {}/{} web_static".format(directory, archive))
    except:
        return None

    print("Packing web_static to " + archive) 
    size = os.stat(archive).st_size
    print('web_static packed: {} -> {}Bytes'.format(path, size))

    return archive
