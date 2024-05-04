#!/usr/bin/python3
"""
Deletes out-of-date archives
fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
    """

import os
from fabric.api import *

env.hosts = ['100.26.122.117', '34.204.101.210']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -t").split()
        archives = [a for a in archives if "web_static_" in a]
        if len(archives) > number:
            archives_to_delete = archives[number:]  # Archives to delete
            for archive in archives_to_delete:
                run("rm -rf {}".format(archive))
