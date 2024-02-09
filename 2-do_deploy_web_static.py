#!/usr/bin/python3
""" Function that compresses a folder """
from datetime import datetime
from fabric.api import *
import shlex
import os

env.hosts = ['52.86.205.42', '54.82.176.167']
env.user = "ubuntu"

def do_deploy(archive_path):
    """ Deploys """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extracting the filename without path and extension
        archive_filename = os.path.basename(archive_path)
        archive_name = shlex.split(archive_filename)[0]

        releases_path = f"/data/web_static/releases/{archive_name}/"
        tmp_path = f"/tmp/{archive_filename}"

        # Upload the archive to /tmp/
        put(archive_path, "/tmp/")
        
        # Create the releases_path directory
        run(f"mkdir -p {releases_path}")

        # Extract the archive to releases_path
        run(f"tar -xzf {tmp_path} -C {releases_path}")

        # Remove the uploaded archive
        run(f"rm {tmp_path}")

        # Move the contents of web_static to releases_path
        run(f"mv {releases_path}web_static/* {releases_path}")

        # Remove the now redundant web_static directory
        run(f"rm -rf {releases_path}web_static")

        # Remove the existing /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a symbolic link to the new version
        run(f"ln -s {releases_path} /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
