#!/usr/bin/env bash

curl http://peak.telecommunity.com/dist/ez_setup.py > /tmp/ez_setup.py
sudo python /tmp/ez_setup.py -U setuptools

sudo easy_install virtualenv
sudo easy_install virtualenvwrapper

PYTHON_BASE=$(dirname `which python`)

touch ~/.profile
mkdir ~/.virtualenvs

if [ ! "$(grep WORKON_HOME ~/.profile)"  ]
    then echo "
export WORKON_HOME=\$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper_bashrc
" >> ~/.profile
fi

source ~/.profile