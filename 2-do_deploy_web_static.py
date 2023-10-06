#!/usr/bin/python3
"""A script that deploys a static content"""

from fabric.api import *
import os

env.hosts = ['54.237.100.5', '52.3.255.219']


def do_deploy(archive_path):
    """A function that deploys and archive to webservers"""
    if not os.path.exists(archive_path):
        return False

    deriv_file = os.path.basename(archive_path)
    deriv_dest = os.path.splitext(deriv_file)[0]
    derived_dest_path = "/data/web_static/releases/{}".format(deriv_dest)

    put(archive_path, '/tmp')

    run("mkdir -p {}".format(derived_dest_path))
    run("tar -xzf /tmp/{} -C {}".format(deriv_file, derived_dest_path))

    run("mv {}/web_static/* {}/"
        .format(derived_dest_path, derived_dest_path))

    run("rm -rf {}/web_static".format(derived_dest_path))
    run("rm /tmp/{}".format(deriv_file))

    with cd('/data/web_static'):
        run('rm -f current')
        run('ln -s {} current'.format(derived_dest_path))

    return True
