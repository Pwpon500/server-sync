#!/usr/bin/python
from subprocess import call
import os

call("echo \"source ~/server-sync/vimrc\" > ~/.vimrc", shell=True)
call("ln -s ~/server-sync/vim ~/.vim", shell=True)

call("echo \". ~/server-sync/bash_aliases\" > ~/.bash_aliases", shell=True)
if os.path.isfile("~/.bashrc"):
    bashrc_content = open("~/.bashrc", "r").read()
    if not bashrc_content.contains("/etc/bashrc"):
        call("echo \"~/server-sync/bashrc\" > ~/.bashrc", shell=True)
else:
    call("echo \"~/server-sync/bashrc\" > ~/.bashrc", shell=True)

call("git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim", shell=True)
call("vim +PluginInstall +qall", shell=True)
