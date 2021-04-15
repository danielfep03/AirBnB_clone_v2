#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the
function do_deploy:
"""

from fabric.api import run, env, put
from os.path import isdir
env.hosts = ['35.196.67.203', '35.229.83.138']


def do_deploy(archive_path):
    """Returns False if the file at the
    path archive_path doesn’t exist
    """
    if isdir(archive_path):
        try:
            file_name = archive_path.split("/")[-1]
            with_out_ext = file_name.split('.')[0]
            path = '/data/web_static/releases'
            put(archive_path, "/tmp/")
            run("mv {} ./tmp".format(archive_path))
            run("mkdir -p {}/{}".format(path, with_out_ext))
            run("tar -xzf /tmp/{} -C {}/{}"
                .format(file_name, path, with_out_ext))
            run("rm /tmp/{}".format(file_name))
            run("mv {}/{}/web_static/* {}/{}"
                .format(path, with_out_ext, path, with_out_ext))
            run("rm -rf {}/{}/web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s {}/{} /data/web_static/current"
                .format(path, with_out_ext))
        except:
            return(False)
    else:
        return(False)
    return(True)
