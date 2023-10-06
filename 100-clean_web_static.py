#!/usr/bin/python3
"""Deletes out-of-date archive"""

from fabric.api import *
from pathlib import Path
import os

env.hosts = ['54.237.100.5', '52.3.255.219']


def do_clean(number=0):
    """Function that will clean-up old archive"""
    number = 1 if number == 0 else int(number)

    fileNames = [Path(i) for i in os.listdir("versions")]
    for fullPath in fileNames[:-number]:
        local(f"rm -r versions/{fullPath.name}")

    with cd("/data/web_static/releases"):
        fileNames = [i for i in run("ls").split()
                     if i.startswith("web_static_")]
        for fullPath in fileNames[:-number]:
            run(f"rm -r {fullPath}")
