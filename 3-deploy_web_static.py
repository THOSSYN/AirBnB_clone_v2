#!/usr/bin/python3
"""A programme that fully deploys the content
   an archive to webservers
"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['54.237.100.5', '52.3.255.219']


def do_pack():
    """Generates a compressed .tgz file from the web_static folder"""

    current_date = datetime.now().strftime('%Y%m%d%H%M%S')

    chek = local("if [ ! -d versions ]; then mkdir versions; fi", capture=True)
    if chek.return_code != 0:
        return None

    arch_path = 'versions/web_static_{}.tgz'.format(current_date)

    archive = local("tar -czvf {} web_static".format(arch_path), capture=True)

    if archive.return_code == 0:
        return arch_path
    else:
        return None


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


def deploy():
    """A function that creates and distributes an archive"""
    result = do_pack()

    if not result:
        return False

    result2 = do_deploy(result)

    return result2
