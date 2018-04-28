# What I expect that should be this project

A tool kit for setup, configure and monitor a Linux Operating System. 

Examples:
- Install programs (Spotify, Google Chrome, etc.).
- Setup .bash preferences (git branch, data, etc.).
- Update SO, some specific program, etc.
- List installed programs and SO configurations.
- Monitoring in real time (reports maybe?)

Support Linux SO:
- Ubuntu (16.04 and 18.04).
- Manjaro (??)
- Arch (??)

## Tasks
MVP with:
- Ubuntu 18.04
- Install Sublime, Chrome, Spotify, ...
- Update
- List installed programs


https://packaging.python.org/tutorials/distributing-packages/
http://python-packaging.readthedocs.io/en/latest/index.html
https://kushaldas.in/posts/building-command-line-tools-in-python-with-click.html

http://click.pocoo.org/5/setuptools/#scripts-in-packages
https://github.com/docopt/docopt


## Setup slave
There are 2 ways of setup a slave machine:

- Install with initial_setup  
With the repo clonned, run initial_setup and it install and sets all the requirements for usage as a slave machine.  
Nothing else needs to be done.


- Enable ssh and zerotier
For the slave machine works as a slave, it's necessary install openssh-server, enable ssh port (22 or another) and install zerotier.  
After install zerotier include the machine to the ZeroTier network.