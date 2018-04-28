

CONF = {
     "git_bash" : {
          "name": "Git BRanch on bash prompt",
          "commands": """
# ref: https://coderwall.com/p/fasnya/add-git-branch-name-to-bash-prompt
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="[\$(date +%k:%M:%S)] \\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
"""
     },
}
