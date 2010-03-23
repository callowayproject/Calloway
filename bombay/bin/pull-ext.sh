#!/bin/bash
if [ "$VIRTUAL_ENV" = "" ]; then
    echo "You must be in a virtualenv environment. Type workon for a list."
    exit
fi

FILES=$VIRTUAL_ENV/src/*

for f in $FILES
do
    if [ -d $f ] 
    then
        cd $f
        if [ -e .git ] 
        then
            git pull origin master
        elif [ -e .bzr ] 
        then
            bzr merge
        elif [ -e .hg ]
        then
            hg pull
        elif [ -e .svn ]
        then
            svn up
        fi
    fi
done