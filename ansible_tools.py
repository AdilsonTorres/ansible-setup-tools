#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
import click
import libs.programs as _p
import libs.configuration as _conf
import json

ROOT_PATH = sys.path[0]

SETUP = {
    "question": "Type of configuration",
    "choices": ["all", "personalized", ],
    "default_choice": 1,
}


HOSTS = ["me", "others"]

ENV_PATH = "venv/bin/"


def ask_question(question, choices, default=None):
    print("\n\n" + question)
    ask_choices = ""

    for i in range(len(choices)):
        ask_choices += "{}. ".format(i+1) + choices[i] + "\n"

    if default:
        ask_choices += "Response (default {}): ".format(default)
    else:
        ask_choices += "Response: "

    answer = input(ask_choices)

    if not answer and default:
        return default - 1

    possible_options = [i for i in range(1, len(choices)+1)]

    while not answer.isdigit() or int(answer) not in possible_options:
        print("Invalid answer, please choose from the options.\n")
        answer = input(ask_choices)

        if not answer and default:
            return default - 1

    return int(answer) - 1


@click.group()
def main():
    """ Script with tools and setup configuration for Linux machines """
    pass


@main.command()
@click.option("--host", default=HOSTS[0], type=click.Choice(HOSTS),
              help="Machine to apply configurations", show_default=True)
def config(host):
    print(_conf.CONF["git_bash"])
    index_answer = ask_question(SETUP["question"], SETUP["choices"], SETUP["default_choice"])
    pass


@main.command()
@click.option("--host", default=HOSTS[0], type=click.Choice(HOSTS),
              help="Machine to apply configurations", show_default=True)
def setup(host):
    """ Setup configurations """
    os.environ["ANSIBLE_CONFIG"] = "/home/adilson/Ansible/ansible-setup-tools/ansible.cfg"
    index_answer = ask_question(SETUP["question"], SETUP["choices"], SETUP["default_choice"])

    # command_list = [ENV_PATH + 'ansible-playbook', '-i', ]
    command_list = [ENV_PATH + 'ansible-playbook', ]

    # if host == 'me':
        # command_list.append('localhost')

    extra_vars = ""
    command_list.append('--extra-vars')

    if host =='me':
        extra_vars += "host={} ".format('localhost')
    command_like = False
    package_like = False
    command_apps = None
    package_apps = None

    if SETUP["choices"][index_answer] == "all":
        for app in _p.PROGRAMS:
            if _p.PROGRAMS[app]['type'] == 'command':
                command_like = True
                if command_apps:
                    command_apps.update({app: _p.PROGRAMS[app]})
                else:
                    command_apps = {app: _p.PROGRAMS[app]}
            else:
                package_like = True
                if package_apps:
                    package_apps.update({app: _p.PROGRAMS[app]})
                else:
                    package_apps = {app: _p.PROGRAMS[app]}

    if command_apps:
        extra_vars += "command_apps={} ".format(json.dumps(command_apps, separators=(',', ':')))
    if package_apps:
        extra_vars += "package_apps={} ".format(json.dumps(package_apps, separators=(',', ':')))

    if command_like:
        extra_vars += "command=libs/tasks/command.yml "
    if package_like:
        extra_vars += "package=libs/tasks/package.yml "

    command_list.append(extra_vars)
    command_list.append("setup.yml")

    print("\ncommand list: {}\n".format(command_list))
    process = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while process.poll() is None:
        out = process.stdout.readline()
        output = out.decode('UTF-8')
        sys.stdout.write(output)
        sys.stdout.flush()


if __name__ == '__main__':
    main()
