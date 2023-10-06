#!/usr/bin/python3
"""A programme that fully deploys the content
   an archive to webservers
"""
from 2-do_deploy_web_static import do_deploy
from 1-pack_web_static import do_pack
from fabric.api import *

env.hosts = ['54.237.100.5', '52.3.255.219']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def deploy():
    """A function that creates and distributes an archive"""
    result = do_pack()

    if not result:
        return False

    result2 = do_deploy(result)

    return result2
