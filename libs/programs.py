

PROGRAMS = {
    "spotify": {
        "type": "command",
        "commands": [
            "snap install spotify",
        ]
    },
    "chrome": {
        "type": "command",
        "commands": [
            "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb",
            "dpkg -i google-chrome-stable_current_amd64.deb",
            "rm google-chrome-stable_current_amd64.deb",
        ],
    },
    "sublime": {
        "type": "command",
        "commands": [
            "snap install sublime-text --classic",
        ]
    },
    "pycharm": {
        "type": "command",
        "commands": [
            "snap install pycharm-professional --classic",
        ],
    },
    "virtualbox": {
        "type": "package",
    },
    "vim": {
        "type": "package",
    },
}
