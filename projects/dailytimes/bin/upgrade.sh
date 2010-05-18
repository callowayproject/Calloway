#!/bin/bash
if [ "$VIRTUAL_ENV" = "" ]; then
    echo "You must be in a virtualenv environment. Type workon for a list."
    exit
fi

git pull origin master
bin/pull-ext.sh