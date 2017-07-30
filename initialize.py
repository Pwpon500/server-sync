#!/usr/bin/python
from subprocess import call
import os

packages = "vim fish figlet vlan bridge-utils tcpdump mdadm"
kvm_packages = "bridge-utils mdadm virtinst virt-manager qemu-kvm libvirt-clients libvirt-daemon-system"

server_type = raw_input("Is this a kvm host? (y/n)")
if server_type == "y":
    packages += kvm_packages

call("apt-get install vim fish figlet vlan bridge-utils tcpdump mdadm -y", shell=True)
call("echo \"source ~/server-sync/vimrc\" > ~/.vimrc", shell=True)
call("ln -s ~/server-sync/vim ~/.vim", shell=True)

call("mkdir ~/.config/fish", shell=True)
call("echo source ~/server-sync/config.fish > ~/.config/fish/config.fish", shell=True)

call("ln -s ~/server-sync/taskrc ~/.taskrc", shell=True)

call("echo \". ~/server-sync/bash_aliases\" > ~/.bash_aliases", shell=True)
if os.path.isfile("~/.bashrc"):
    bashrc_content = open("~/.bashrc", "r").read()
    if not bashrc_content.contains("/etc/bashrc"):
        call("echo \"~/server-sync/bashrc\" > ~/.bashrc", shell=True)
else:
    call("echo \". ~/server-sync/bashrc\" > ~/.bashrc", shell=True)

call("git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim", shell=True)
call("vim +PluginInstall +qall", shell=True)

call("echo '' > /etc/motd", shell=True)
call("rm /etc/update-motd.d/*", shell=True)
call("ln -s ~/server-sync/scripts/20-updates /etc/update-motd.d/20-updates", shell=True)

fishorbash = raw_input("Would you like to use fish or bash? (f/b)")
if fishorbash == "f":
        call("chsh -s /usr/bin/fish", shell=True)
