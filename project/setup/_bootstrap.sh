#!/usr/bin/env bash

VE_PATH=`which virtualenv`
VEW_PATH=`which virtualenvwrapper_bashrc`

if [ -z $VE_PATH ]
then
    sudo easy_install virtualenv
fi

if [ -z $VEW_PATH ]
then
    sudo easy_install virtualenvwrapper
    mkdir ~/.virtualenvs
    echo "Put the following lines in your .bashrc, .profile or environment
    export WORKON_HOME=\$HOME/.virtualenvs
    source virtualenvwrapper_bashrc"
fi


