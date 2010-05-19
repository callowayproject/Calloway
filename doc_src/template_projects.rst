
=================
Template Projects
=================

The ``create_project`` script
=============================

The first step in any Calloway project is using the ``create_project.py`` script. This script copies a project template to a specified directory and renames files and placeholders within files.

You can have any number of template projects; the script asks you for the path at runtime. A sample template project is included in the repository.


Before running the script
=========================

The script does not require Calloway to run. Just Python and the python packages virtualenv and virtualenvwrapper.

1. Install Python if necessary.
2. Get the latest ``create_project.py`` script at 
   `<http://www.callowayproject.com/downloads/create_project.py>`_\ .
3. Install the python packages::

   	pip install virtualenv
   	pip install virtualenvwrapper

   or ::

   	easy_install virtualenv
   	easy_install virtualenvwrapper


Running the script
==================

The ``creat_project.py`` script defaults to an interactive prompt for information. There are command options, but none are required. Any option not specified by a command option is prompted. To run the script, change to the directory to which you downloaded the ``create_project.py`` and run it::

	python create_project.py


.. program:: create_project.py

.. cmdoption:: -a <adminstrator name>, --admin <administrator name>

   **Description** The name of the administrator for the site.

   **Default** It defaults to the current user's login name.

   **Placeholder** ``$$$$NAME$$$$``

.. cmdoption:: -e <administrator email>, --email <administrator email>

   **Description** The email address of the website administrator.

   **Default** None

   **Placeholder** ``$$$$EMAIL_ADDRESS$$$$``

.. cmdoption:: -n <project name>, --name <project name>

   **Description** The name of the project you are creating

   **Default** None

   **Placeholder** ``$$$$PROJECT_NAME$$$$``

.. cmdoption:: -v <virtualenv name>, --virtualenv <virtualenv name>

   **Description** The name of the Python virtualenv to create.

   **Default** None, although the interactive prompt defaults to the project name.

   **Placeholder** ``$$$$virtenv$$$$``

.. cmdoption:: -d <destination path>, --dest <destination path>

   **Description** Where to save the project. Relative paths are accepted.

   **Default** None, although the interactive prompt defaults to the current working directory.

   **Placeholder** None

.. cmdoption:: -t <template path>, --dest <template path>

   **Description** The path to the project template. Relative paths are accepted.

   **Default** None

   **Placeholder** None

The Sample Project Template Structure
=====================================

The sample project template directory structure is a recommended layout, but by no means required. We'll go through the parts to explain how you might want to customize it for your needs.

apps
****

You an put your Django applications in many places. We recommend two (or possibly three, if you count ``lib``\ ): ``apps`` and ``site-packages``\ .

``apps`` is for project-specific apps. These are apps that will only make sense in this project, like custom import and export applications. If your projects all need the same application, but it is always customized from a template, you could put the template code here in the project template. Then it is ready to customize for each project.

bin
***

We use bin for helpful development scripts that are executed independently from the command line. For example, pulling changes to all installed packages. 

``ext-status.sh``
	This example script goes through pip "editable" packages and lists local changes.

``install.sh``
	A shortcut to install everything in a ``requirements.txt`` file as well as making a symlink from the "editable" packages directory to the local directory, and adds a ``postactivate`` script for ``virtualenvwrapper`` to switch to the appropriate directory upon activation.

``pull-ext.sh``
	If you are using "editable" packages (very nice for development) this script will attempt to update all the packages.

``push-ext.sh``
	The opposite of ``pull-ext.sh``\ , this pushes out all local commits. It currently only works with git.

``upgrade.sh``
	This example script uses git to pull down the latest changes and then executes the ``pull-ext.sh`` script.

conf
****

Any configuration file required to run your site sits in here. Here placeholders make all the difference. Since most of your projects probably use the same basic Apache, lighttpd, nginx, or wsgi configurations, with a few things changed, the placeholders from the ``create_project.py`` script takes care of these.

You'll notice sample wsgi and apache2 configuration files that use placeholders in the file name, as well as within the files. We symlink these files to the appropriate configuration directory (for example the apache2 configuration is symlinked to ``/etc/apache2/sites-available/``\ ) so that updates are maintained in source control and automatically updated on production servers.

``$$$$PROJECT_NAME$$$$.wsgi``
	The default wsgi file to use with Apache and mod_wsgi. The placeholder renames the file to the project name (so in a project named "coolsite" the file becomes "coolsite.wsgi").
	
	There are also placeholders within the file to set up the paths. It adds the virtualenv's site-packages to the Python path with::
	
		site.addsitedir('/home/webdev/$$$$PROJECT_NAME$$$$/.virtualenvs/$$$$PROJECT_NAME$$$$/lib/python2.5/site-packages')

``apache2-$$$$PROJECT_NAME$$$$``
	For Apache deployment, this is the default configuration file. There are many placeholders used to specify various Apache configuration options and file paths.

lib
***

Put any project-specific library packages in ``lib``\ . A library is any python package that doesn't require inclusion in Django's ``INSTALLED_APPS`` setting.

static
******

This is where project-specific media files that don't change (often) such as CSS, images, and Javascript files. User uploaded files should be stored somewhere else, to mitigate the opportunity for malicious hacking.

Calloway uses django-staticmediamgr to copy and combine media files from all installed apps and other specified sources to one directory. This is helpful for hosting media on a separate server.

templates
*********

No, the name isn't deceiving; you put templates for your site in here. There are a few basic ones offered as a start. You *will* want to modify these and improve upon them.

