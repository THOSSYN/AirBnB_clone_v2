#!/usr/bin/python3
"""Compresses a folder into a zip file"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """Generates a compressed .tgz file from the web_static folder"""

    # Get the current date and time
    current_date = datetime.now().strftime('%Y%m%d%H%M%S')

    chek = local("if [ ! -d versions ]; then mkdir versions; fi", capture=True)
    if chek.return_code != 0:
        return None

    archive_path = f'versions/web_static_{current_date}.tgz'

    archive = local(f"tar -czvf {archive_path} web_static", capture=True)

    if archive.return_code == 0:
        return archive_path
    else:
        return None
