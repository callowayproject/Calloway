
===============
Getting Started
===============

1. Install the project template

2. From the command line, change to that directory

3. Execute ``python start_project.py`` and answer the questions.

   The script should copy the template project to the specified folder, replacing the placeholder elements in transit. Then it will create a virtualenv, install pip, and execute an initial ``pip install -r setup/requirements.txt``\ . That should at least install Django and Calloway.

4. Type ``workon <virtualenv name>`` using the virtual environment name you specified in the script.

5. Customize the ``settings.py`` file, specifically changing the application bundles included in the ``INSTALLED_APPS`` setting. The example template uses::

	INSTALLED_APPS = APPS_CORE + \
	    APPS_ADMIN + \
	    APPS_STAFF + \
	    APPS_REVERSION + \
	    APPS_STORIES + \
	    APPS_CALLOWAY_DEFAULT + \
	    APPS_MPTT + \
	    APPS_CATEGORIES + \
	    APPS_COMMENT_UTILS + \
	    APPS_FRONTEND_ADMIN + \
	    APPS_MEDIA + \
	    APPS_UTILS + \
	    APPS_REGISTRATION + \
	    APPS_TINYMCE 

6. Remove any application bundles that you don't want or need, and add any others by adding them in an additional tuple like::

	INSTALLED_APPS = APPS_CORE + \
	    APPS_ADMIN + \
	    APPS_STAFF + \
	    ...
	    APPS_TINYMCE + (
	        "cheese_chop",
	        "dead_parrot",
	        "holy_grail",
	    )

7. Type ``./manage.py generate_reqs setup/calloway_reqs.txt``

6. Type ``pip install -r setup/requirements.txt``
