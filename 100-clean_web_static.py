#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""
from fabric.api import *
from fabric.operations import run, local
import os

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = int(number)

    # Keep at least one version if number is 0 or 1
    if number == 0:
        number = 1

    # Deleting files in the local directory
    local("ls -t versions | tail -n +{} | xargs rm -rf".format(number + 1))

    # Deleting files on remote servers
    run("ls -t /data/web_static/releases | grep 'web_static_' | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number + 1))
