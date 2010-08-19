.. _media_handling:

===================
Media Configuration
===================

Calloway allows for a range of media serving options. While many Django users are used to having a single directory in which everything resides, others may need to have media hosted somewhere else, and if you allow for user uploads, you may want those stored somewhere different from your regular media.

Three Different Kinds of Media
==============================

All media is not created equal, and you may want to handle different media, well, differently. Here are a few types we've identified.

**assets**
	Assets are files that your staff uploads, such as photos, documents and audio recordings. Django 1.1 or greater allows for custom media storage, which Calloway can use to separate the staff uploads from applications such as Massmedia from user uploads from applications like a user profile.

**static**
	Static files are files specifically for the website, such as CSS, Javascript, and images. You should store these files in your repository. Many times you will want to combine some and minify or otherwise optimize others.

**uploads**
	You might not allow user uploads, but if you ever do, you will want to keep these files separate from others.

Media Management in Calloway
============================

By default, Django wants to store all media in the same place. Segregating different types of media requires a bit of reconfiguration to make it work. The settings here assumes that static or website media is stored in the repository in a directory named ``static``\ . Assets and uploads are stored in directories within a directory named ``media`` where ``media`` is *not* in the repository.

.. image:: images/callowaymediahandling.png





``MEDIA_URL_PREFIX`` and ``MEDIA_ROOT_PREFIX`` settings
*******************************************************

These settings aren't standard Django settings, but it makes it easier to configure the multiple urls we need. If you are going to store production media on a separate server or location from your development media.

The sample project template configures these::

	try:
	    from local_settings import MEDIA_URL_PREFIX
	except ImportError:
	    MEDIA_URL_PREFIX = "http://media.example.com/"
	try:
	    from local_settings import MEDIA_ROOT_PREFIX
	except ImportError:
	    MEDIA_ROOT_PREFIX = '/nfs-media/website/'

This configuration allows for media to be handled differently during development than deployment, and allows for custom media storage to utilize them.

``MEDIA_ROOT`` and ``MEDIA_URL`` settings
*****************************************

This is the default place that Django looks for media. We are going to use this for user-generated content. ::

	try:
	    from local_settings import MEDIA_ROOT
	except ImportError:
	    MEDIA_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'ugc')
	MEDIA_URL = '%sugc/' % MEDIA_URL_PREFIX

``STATIC_MEDIA`` and ``STATIC_URL`` settings
********************************************

This is a proposed addition to Django's default settings. Other projects, such as `Pinax <http://pinaxproject.com/>`_, are already using this convention for their website media. Static Media Manager has a context processor that makes ``STATIC_URL`` available to the template. ::

	try:
	    from local_settings import STATIC_ROOT
	except ImportError:
	    STATIC_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'static')
	STATIC_URL = "%sstatic/" % MEDIA_URL_PREFIX

Massmedia storage setup
***********************

Massmedia allows for the configuration of a default storage system to be used for all types of media, and separate configurations to override the default for each type of media. In the ``apps`` directory is ``media_storage.py``\ . This contains a custom file storage system for django. The following setting sets the correct storage place using the ``MEDIA_URL_PREFIX`` and ``MEDIA_ROOT_PREFIX`` settings. ::

	MMEDIA_DEFAULT_STORAGE = 'media_storage.MediaStorage'

StaticMediaMgr settings
***********************

The tool we developed for managing application static media as well as site-specific static media is StaticMediaMgr. It can copy, compress, minify and join files in a configurable way.

First, we need to handle application media. StaticMediaMgr looks in every application in ``INSTALLED_APPS`` for a ``media`` directory. All of these directories need a place to copy. We will set it to the destination static media directory.

.. note:: 
   
   This media is copied *before* the items in the ``static`` directory. This allows us to override a specific media's items similarly to overriding templates.

::

	STATIC_MEDIA_APP_MEDIA_PATH = STATIC_ROOT

We can have StaticMediaMgr recursively copy multiple directories to different places. ::

	STATIC_MEDIA_COPY_PATHS = (
	    {'from': os.path.join(CALLOWAY_ROOT, 'media'), 'to': STATIC_ROOT},
	    {'from': 'static', 'to': STATIC_ROOT},
	)

Last, but not least, we must configure the compression. During development, we don't want it, but we do want it for production::

	STATIC_MEDIA_COMPRESS_CSS = not DEBUG
	STATIC_MEDIA_COMPRESS_JS = not DEBUG


Ignoring the right things
*************************

The ``.gitignore`` file should contain several things::

	*.pyc
	.svn
	.DS_Store
	local_settings.py
	externals
	pip-log.txt
	dev.db
	media2/
	media/

