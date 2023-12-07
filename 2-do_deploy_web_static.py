#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/" + no_ext + "/"

        run("mkdir -p " + path)
        run("tar -xzf /tmp/" + file_name + " -C " + path)
        run("rm /tmp/" + file_name)
        run("mv " + path + "web_static/* " + path)
        run("rm -rf " + path + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + path + " /data/web_static/current")
        return True
    except:
        return False
