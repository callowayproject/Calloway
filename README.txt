GETTING SET UP FOR THE FIRST TIME
---------------------------------

1. Bootstrap your environment. This only needs to be done once:

    ./setup/_bootstrap.sh


2. Create a virtual environment (it doesn't need to be named bombay,
   but name it something you'll remember):

    mkvirtualenv bombay


3. Install the "pip" Python package manager in the new virtual environment:

    easy_install pip


4. Upgrade to the latest version of the packages:

    ./bin/upgrade.sh

5. Link the source directory into the project folder for easier access

    ln -s ~/.virtualenvs/bombay/src/ externals


WHAT YOU SHOULD DO PERIODICALLY
-------------------------------

1. Switch to the correct virtual environment:

    workon bombay


2. Upgrade to the latest version of the packages:

    ./bin/upgrade.sh



WHAT YOU SHOULD DO EVERY DAY
----------------------------

1. Upgrade to the latest code:

    git pull


2. Switch to the correct virtual environment:

    workon bombay


3. Start your local development server:

    python manage.py runserver 0.0.0.0:8000