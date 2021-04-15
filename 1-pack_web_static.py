#!/usr/bin/python3
""" Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """all archives web_static"""
    my_date = datetime.now().strftime('%Y%m%d%H%M%S')
    try:
        if not isdir("versions"):
            local("mkdir versions")
        doc = "web_static_{}.tgz".format(my_date)
        local("tar -zcvf versions/{} web_static".format(doc))
        return doc
    except:
        return None
