#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive
    """
    try:
        local("mkdir -p versions")
        now = datetime.now()
        file_format = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)
        local("tar -cvzf {} web_static".format(file_format))
        return file_format
    except:
        return None
