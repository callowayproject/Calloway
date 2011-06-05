
============
Installation
============

There are several parts to the Calloway project that are not dependent upon each other, but work great in tandem.

.. _installation_start_project_script:

start_project.py script
=======================

The ``start_project.py`` script is an interactive command-line program for building a Django project from a template project, based on code from `Eric Florenzano <http://www.eflorenzano.com/>`_. The template project isn't anything special except that any placeholders for certain variables are replaced during the project creation.

View the script at https://gist.github.com/444408 or download the script directly from https://gist.github.com/gists/444408/download\ . Once you download the script, you will need to decompress it.

::

	$ curl https://gist.github.com/gists/444408/download | tar -zxv
	
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	102  2058  102  2058    0     0   7629      0 --:--:-- --:--:-- --:--:--  9942
	x gist444408-597f127451c5cd81e599753224b4e9fb133bd3eb/
	x gist444408-597f127451c5cd81e599753224b4e9fb133bd3eb/start_project.py

You can move the script anywhere you want from here, however it is handy to rename the folder containing the script and download the :ref:`installation_project_template` into it. ::

	$ mv gist444408-597f127451c5cd81e599753224b4e9fb133bd3eb project_template
	$ cd project_template


.. _installation_project_template:

Project Template
================

The example project template is meant to be a starting point. It is likely that you will have several templates for different types of sites or deployments. Download the ``project_tmpl`` code from 
`github <https://github.com/callowayproject/project_tmpl/downloads>`_ and decompress it. Alternatively, you can clone it using ``git`` if you wish to keep up-to-date with any changes we make to it.

::

	$ curl -L  https://github.com/callowayproject/project_tmpl/tarball/master | tar -zvx
	
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	100 61440  100 61440    0     0   254k      0 --:--:-- --:--:-- --:--:--  254k
	
	x callowayproject-project_tmpl-0dcbf69/
	x callowayproject-project_tmpl-0dcbf69/.gitignore
	x callowayproject-project_tmpl-0dcbf69/__init__.py
	...

Make any changes to this template you wish. It's *your* project template now.


.. _installation_calloway_application:

Calloway Application
====================

The Calloway application is just like any other Django application. You can install it in any typical way, using ``pip`` or ``easy_install`` although the suggested method is to include Calloway in the requirements file in your project.

The example project template includes ``calloway`` as a requirement in ``setup/requirements.txt``\ . When you execute ``pip install -r setup/requirements.txt``\ , ``pip`` will install all other requirements (Django, for example) as well as Calloway. You can add the specific version of Calloway to your requirements file (e.g. ``calloway==0.2``) if you want. We didn't want to tie the project template too closely with the Calloway Application version as the two parts will change at different rates.