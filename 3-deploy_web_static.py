#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""
from fabric.api import *
from os.path import isfile

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_pack():
    """
    Generate a .tgz archive
    """
    local("mkdir -p versions")
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(now)
    local("tar -cvzf {} web_static".format(archive_path))
    return archive_path if isfile(archive_path) else None

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        no_ext = archive_path.split("/")[1].split(".")[0]
        path = "/data/web_static/releases/" + no_ext + "/"
        run("mkdir -p " + path)
        run("tar -xzf /tmp/" + no_ext + ".tgz -C " + path)
        run("rm /tmp/" + no_ext + ".tgz")
        run("mv " + path + "web_static/* " + path)
        run("rm -rf " + path + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + path + " /data/web_static/current")
        return True
    except:
        return False

def deploy():
    """
    Creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
