#!/usr/bin/python3
"""
 generates a .tgz archive from the contents
of the web_static folder
and deploy it to web servers
"""

from datetime import datetime
from fabric.api import local, put, run, env
import os.path

env.hosts = ['52.86.205.42', '54.82.176.167']


def do_deploy(archive_path):
    """
    Deploy archive to web servers
    """
    if not os.path.exists(archive_path):
        print("Error: Archive does not exist.")
        return False

    arch_name = os.path.basename(archive_path)
    arch_name_nex = os.path.splitext(arch_name)[0]
    re_path = f"/data/web_static/releases/{arch_name_nex}"
    up_path = f'/tmp/{arch_name}'

    try:
        put(archive_path, up_path)
        run(f'mkdir -p {re_path}')
        run(f'tar -xzf /tmp/{arch_name} -C {re_path}/')
        run(f'rm {up_path}')
        mv = f'mv {re_path}/web_static/* {re_path}/'
        run(mv)
        run(f'rm -rf {re_path}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {re_path} /data/web_static/current')
        print("Deployment successful.")
        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
