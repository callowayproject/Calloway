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
            git status
        elif [ -e .bzr ] 
        then
            bzr status
        elif [ -e .hg ]
        then
            hg status
        elif [ -e .svn ]
        then
            svn status
        fi
    fi
done