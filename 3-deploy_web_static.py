#!/usr/bin/python3
"""
Write a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your
web servers, using the function deploy:
"""
from fabric.api import run, env, put
env.hosts = ['35.196.67.203', '35.229.83.138']


def deploy():
    """
    script should take the following steps
    """

