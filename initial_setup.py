#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import sys


def initial_setup():
    # Necessary for install programs and edit protected files.
    if os.geteuid() != 0:
        print("Script must need root access")
        subprocess.call(['sudo', 'python3', *sys.argv])

    # Install pip for python3
    subprocess.call("sudo apt-get install -y python3-distutils", shell=True)
    subprocess.call("wget https://bootstrap.pypa.io/get-pip.py", shell=True)
    subprocess.call("sudo python3 get-pip.py", shell=True)
    subprocess.call("rm get-pip.py", shell=True)

    # install virtualenv and create one
    subprocess.call("sudo pip install virtualenv", shell=True)
    subprocess.call("sudo pip install cryptography --upgrade", shell=True)
    subprocess.call("virtualenv --system-site-packages venv", shell=True)
    subprocess.call("venv/bin/pip install --editable .", shell=True)

    # Creates an alias for use the script
    subprocess.call("echo 'alias ansible_tools=$(pwd)/venv/bin/ansible_tools'' >> ~/.bashrc",
                    shell=True)
    subprocess.call("source ~/.bashrc", shell=True)

# Maybe use ansible for now on to install and configure files

    # Install openssh-server
    subprocess.call("sudo apt install openssh-server", shell=True)

    filename = '/etc/ssh/sshd_config'

    subprocess.call("sudo cp {0} {0}.original".format(filename), shell=True)

    with open(filename, 'a') as file:
        file.write("Port 22\n")
    file.close()

    subprocess.call("sudo systemctl restart sshd.service", shell=True)
# TODO: Include a self-kill option for clean up all the repo. For slave machines only.


if __name__ == "__main__":
    initial_setup()
