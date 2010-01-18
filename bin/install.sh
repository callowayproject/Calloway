#!/usr/bin/env bash

if [ "$VIRTUAL_ENV" = "" ]; then
    echo "You must be in a virtualenv environment. Type workon for a list."
    exit
fi

PWD=`pwd`
POSTACTIVATE=$VIRTUAL_ENV/bin/postactivate

if [ -e externals ]; then
    echo 'Externals link exists.'
else
    echo 'Creating link: externals.'
    ln -s $VIRTUAL_ENV/src externals
fi

if [ -e $POSTACTIVATE ]; then
    echo 'Postactivate script exists.'
else
    echo 'Creating postactivate script.'
    cat > $POSTACTIVATE <<END
    #!/bin/bash/
    cd $PWD
END
    chmod +x $POSTACTIVATE
fi

pip install -U -r setup/requirements.txt
rm -Rf src
rm -Rf build
rm -Rf pip-log.txt