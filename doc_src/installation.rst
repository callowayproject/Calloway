
============
Installation
============

There are two parts to the Calloway project that are not dependent upon each other, but work great in tandem.


Project Template
================

The project template is the first part. It is based on code from Eric Florenzano. An example project template is included, but you can specify any directory you want as your template project.

To install the project tempate:

1. Download the ``project_tmpl`` script from ``www.callowayproject.com/downloads/project_tmpl.tar.gz``

2. Decompress the file.


Calloway Application
====================

The Calloway application is just like any other Django application. You can install it in any typical way, although the suggested method is to include Calloway in the requirements file in your project.

The example project template includes ``calloway`` as a requirement in ``setup/requirements.txt``\ . When you execute ``pip install -r setup/requirements.txt``\ , ``pip`` will install all other requirements (Django, for example) as well as Calloway. You can add the specific version of Calloway to your requirements file (e.g. ``calloway==0.2``) if you want. We didn't want to tie the project template too closely with the Calloway Application version as the two parts will change at different rates.