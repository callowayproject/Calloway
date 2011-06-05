
===============
Getting Started
===============

#. Download the :ref:`installation_start_project_script` ::

	$ curl http://gist.github.com/gists/444408/download | tar -zxv
	$ mv gist444408-597f127451c5cd81e599753224b4e9fb133bd3eb project_template
	$ cd project_template

#. Download the example :ref:`installation_project_template` ::

	$ curl -L  https://github.com/callowayproject/project_tmpl/tarball/master | tar -zvx
	$ mv callowayproject-project_tmpl-0dcbf69 project_tmpl
	
#. Execute::

	$ python start_project.py

   and answer the questions.

   ::

	$ python start_project.py 
	Project name: sampleproject
	Administrator e-mail address: admin@sampleproject.com
	Destination directory (currently at /home/demo/project_template): 
	Project template directory [/home/demo/project_tmpl]: ./project_tmpl
	Virtual environment name (e.g. sampleproject): 
	Copying /home/demo/quickstart/project_tmpl/__init__.py to /home/demo/quickstart/sampleproject/__init__.py
	Copying /home/demo/quickstart/project_tmpl/manage.py to /home/demo/quickstart/sampleproject/manage.py
	Copying /home/demo/quickstart/project_tmpl/menu.py to /home/demo/quickstart/sampleproject/menu.py
	Copying /home/demo/quickstart/project_tmpl/settings.py to /home/demo/quickstart/sampleproject/settings.py
	Copying /home/demo/quickstart/project_tmpl/urls.py to /home/demo/quickstart/sampleproject/urls.py
	Copying /home/demo/quickstart/project_tmpl/apps/media_storage.py to /home/demo/quickstart/sampleproject/apps/media_storage.py
	Copying /home/demo/quickstart/project_tmpl/apps/yourappshere.txt to /home/demo/quickstart/sampleproject/apps/yourappshere.txt
	Copying /home/demo/quickstart/project_tmpl/bin/ext-status.sh to /home/demo/quickstart/sampleproject/bin/ext-status.sh
	Copying /home/demo/quickstart/project_tmpl/bin/install.sh to /home/demo/quickstart/sampleproject/bin/install.sh
	Copying /home/demo/quickstart/project_tmpl/bin/pull-ext.sh to /home/demo/quickstart/sampleproject/bin/pull-ext.sh
	Copying /home/demo/quickstart/project_tmpl/bin/push-ext.sh to /home/demo/quickstart/sampleproject/bin/push-ext.sh
	Copying /home/demo/quickstart/project_tmpl/bin/upgrade.sh to /home/demo/quickstart/sampleproject/bin/upgrade.sh
	Copying /home/demo/quickstart/project_tmpl/conf/$$$$PROJECT_NAME$$$$.wsgi to /home/demo/quickstart/sampleproject/conf/sampleproject.wsgi
	Copying /home/demo/quickstart/project_tmpl/conf/apache2-$$$$PROJECT_NAME$$$$ to /home/demo/quickstart/sampleproject/conf/apache2-sampleproject
	Copying /home/demo/quickstart/project_tmpl/conf/nginx-$$$$PROJECT_NAME$$$$ to /home/demo/quickstart/sampleproject/conf/nginx-sampleproject
	Copying /home/demo/quickstart/project_tmpl/lib/yourlibshere.txt to /home/demo/quickstart/sampleproject/lib/yourlibshere.txt
	Copying /home/demo/quickstart/project_tmpl/setup/_bootstrap.sh to /home/demo/quickstart/sampleproject/setup/_bootstrap.sh
	Copying /home/demo/quickstart/project_tmpl/setup/calloway_reqs.txt to /home/demo/quickstart/sampleproject/setup/calloway_reqs.txt
	Copying /home/demo/quickstart/project_tmpl/setup/requirements.txt to /home/demo/quickstart/sampleproject/setup/requirements.txt
	Copying /home/demo/quickstart/project_tmpl/templates/404.html to /home/demo/quickstart/sampleproject/templates/404.html
	Copying /home/demo/quickstart/project_tmpl/templates/500.html to /home/demo/quickstart/sampleproject/templates/500.html
	Copying /home/demo/quickstart/project_tmpl/templates/base.html to /home/demo/quickstart/sampleproject/templates/base.html
	Copying /home/demo/quickstart/project_tmpl/templates/site_base.html to /home/demo/quickstart/sampleproject/templates/site_base.html
	Copying /home/demo/quickstart/project_tmpl/templates/admin/base_site.html to /home/demo/quickstart/sampleproject/templates/admin/base_site.html
	Copying /home/demo/quickstart/project_tmpl/templates/admin/change_form.html to /home/demo/quickstart/sampleproject/templates/admin/change_form.html
	Copying /home/demo/quickstart/project_tmpl/templates/admin/positions/selector.html to /home/demo/quickstart/sampleproject/templates/admin/positions/selector.html
	Making the virtual environment (sampleproject)...
	New python executable in sampleproject/bin/python
	Installing distribute..................................................................................................................................................................................done.
	virtualenvwrapper.user_scripts Creating /home/demo/.virtualenvs/sampleproject/bin/predeactivate
	virtualenvwrapper.user_scripts Creating /home/demo/.virtualenvs/sampleproject/bin/postdeactivate
	virtualenvwrapper.user_scripts Creating /home/demo/.virtualenvs/sampleproject/bin/preactivate
	virtualenvwrapper.user_scripts Creating /home/demo/.virtualenvs/sampleproject/bin/postactivate
	Searching for pip
	Best match: pip 0.6.3
	Processing pip-0.6.3-py2.6.egg
	pip 0.6.3 is already the active version in easy-install.pth
	Installing pip script to /home/demo/.virtualenvs/sampleproject/bin

	Using /home/demo/.virtualenvs/sampleproject/lib/python2.6/site-packages/pip-0.6.3-py2.6.egg
	Processing dependencies for pip
	Finished processing dependencies for pip
	Installing requirements...
	Downloading/unpacking calloway
	  Downloading calloway-0.1.10.tar.gz (10.4Mb): 10.4Mb downloaded
	  Running setup.py egg_info for package calloway
	    no previously-included directories found matching 'project'
	    no previously-included directories found matching 'calloway_test'
	Installing collected packages: calloway
	  Running setup.py install for calloway
	    no previously-included directories found matching 'project'
	    no previously-included directories found matching 'calloway_test'
	    changing mode of build/scripts-2.6/generate_reqs.py from 644 to 755
	    changing mode of /Users/coordt/.virtualenvs/sampleproject/bin/generate_reqs.py to 755
	Successfully installed calloway
	Downloading/unpacking Django
	  Downloading Django-1.3.tar.gz (6.2Mb): 6.2Mb downloaded
	  Running setup.py egg_info for package Django
	    warning: no files found matching '*' under directory 'examples'
	Installing collected packages: Django
	  Running setup.py install for Django
	    changing mode of build/scripts-2.6/django-admin.py from 644 to 755
	    warning: no files found matching '*' under directory 'examples'
	    changing mode of /Users/coordt/.virtualenvs/sampleproject/bin/django-admin.py to 755
	Successfully installed Django
	Cleaning up...
   
   
   The script copies the template project to the specified folder, replacing the placeholder elements in transit. Then it creates a virtualenv, installs pip and distribute, and finally executes an initial ``pip install -r setup/requirements.txt`` that should at least install Django and Calloway.

#. Switch to the virtual environment we specified in the script::

	workon sampleproject

#. Customize the ``settings.py`` file, specifically changing the application bundles included in the ``INSTALLED_APPS`` setting. The example template uses::

	INSTALLED_APPS = APPS_DJANGO13_BASE + \
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

   Remove any application bundles that you don't want or need, and add any others by adding them in an additional tuple like::

	INSTALLED_APPS = APPS_CORE + \
	    APPS_ADMIN + \
	    APPS_STAFF + \
	    ...
	    APPS_TINYMCE + (
	        "cheese_shop",
	        "dead_parrot",
	        "holy_grail",
	    )

#. When Calloway is installed, it installs a stand-alone script to dynamically generate a ``pip`` requirements file based on the applications specified in ``INSTALLED_APPS`` that it knows about. It can populate or create a file specified or else it prints the requirements to standard out. ::

	generate_reqs setup/calloway_reqs.txt

#. If you have added any other Django apps or libraries, make sure you update the ``setup/requirements.txt`` file.

#. Finally, to install the new pieces::

	pip install -r setup/requirements.txt

   The example project template includes ``-r setup/calloway_reqs.txt`` at the end of its requirements file. Some packages may need to be compiled. After all the packages are installed you should see something like::

	Successfully installed BeautifulSoup critic django-admin-tools ...
	Cleaning up...

#. Synchronize your database, as you normally would::

	./manage.py syncdb

