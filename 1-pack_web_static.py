#!/usr/bin/python3
""" using fabric 101
"""
from datetime import datetime
from fabric import task
from invoke import run
from os.path import isdir


@task
def do_pack(ctx):
    """generates a tgz achive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("version") is False:
            run("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        run("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None
