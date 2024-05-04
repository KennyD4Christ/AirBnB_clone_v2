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
    number = int(number)

    # Get the list of archives on each server
    with settings(warn_only=True):
        archives_list_1 = run("ls /data/web_static/releases").split()
        archives_list_2 = run("ls /data/web_static/releases").split()

    # Find the minimum number of archives on any server
    min_archives = min(len(archives_list_1), len(archives_list_2))

    # Determine the number of archives to delete
    num_to_delete = min_archives - number
    if num_to_delete <= 0:
        print("Nothing to clean!")
        return

    # Delete the out-of-date archives remotely on both servers
    with cd("/data/web_static/releases"):
        run("ls -t | grep 'web_static_' | tail -n +{} | xargs rm -rf"
            .format(number + 1))

    print("Cleanup completed successfully!")
