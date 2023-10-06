#!/usr/bin/env python3
"""A script that deploys a static content"""

from fabric.api import *
import os

env.hosts = ['54.237.100.5', '52.3.255.219']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """This function distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False

    deriv_file = os.path.basename(archive_path)
    deriv_dest = os.path.splitext(deriv_file)[0]
    derived_dest_path = f"/data/web_static/releases/{deriv_dest}"

    put(archive_path, '/tmp')

    sudo(f"mkdir -p {derived_dest_path}")
    sudo(f"tar -xzf /tmp/{deriv_file} -C {derived_dest_path}")

    run(f"rm /tmp/{deriv_file}")
    
    with cd('/data/web_static'):
        #sudo("unlink /data/web_static/current")
        sudo('rm -f current')
        sudo(f'ln -s {derived_dest_path} current')
        #sudo(f'ln -s {derived_dest_path} /data/web_static/current")

    return True
