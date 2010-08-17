.. _migration:

Migrating an Existing Django Project to Calloway
================================================

For Starters
-------------

To start off, make sure you are using ``virtualenv`` and ``virtualenvwrapper``. If you have not already done so, install them::

    pip install virtualenv virtualenvwrapper
    
Then create a new virtual environment for your new Calloway based project::

    mkvirtualenv newproject

.. note:: Make sure to change your the shbang (first line) in your project's ``manage.py`` to point to the newly installed copy of python in your virtual environment. It should be something like: ``#!/home/user/.virtualenvs/newproject/bin/python``


Activate your new virtual environment and install the Calloway app::

    workon newproject
    pip install calloway

This will install a load of dependencies along with it. To see the full list for future reference, you can generate a requirements file::

    generate_reqs > requirements.txt


Settings
---------

In your project's ``settings.py`` make the following changes.
Add this bit to the top of the file so that the Calloway apps are on your ``sys.path``::

    import os, sys
    import calloway
    
    CALLOWAY_ROOT = os.path.abspath(os.path.dirname(calloway.__file__))
    sys.path.insert(0, os.path.join(CALLOWAY_ROOT, 'apps'))

Then import the default Calloway settings::

    from calloway.settings import *


Now you can alter your ``INSTALLED_APPS`` setting to include the Calloway application bundles.
Prepend your local apps with the bundles like so::

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
        APPS_TINYMCE + \
        ( # Local apps here
            "cheese_shop",
            "dead_parrot",
            "holy_grail",
        )
        
Now you can adjust your media settings.
Below is an example of how to setup the media where the ``static`` folder
contains all of your project's assets and the ``media`` folder is where the new media is copied into for serving. 
For more information on media handling, checkout :ref:`media_handling`::

    try:
        from local_settings import MEDIA_URL_PREFIX
    except ImportError:
        MEDIA_URL_PREFIX = "http://media.example.com/"
    try:
        from local_settings import MEDIA_ROOT_PREFIX
    except ImportError:
        MEDIA_ROOT_PREFIX = '/var/www/media'
    try:
        from local_settings import MEDIA_ROOT
    except ImportError:
        MEDIA_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'ugc')
    try:
        from local_settings import STATIC_ROOT
    except ImportError:
        STATIC_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'static')
        
    
    MEDIA_URL = '%sugc/' % MEDIA_URL_PREFIX
    STATIC_URL = "%sstatic/" % MEDIA_URL_PREFIX
    STATIC_MEDIA_APP_MEDIA_PATH = STATIC_ROOT
    STATIC_MEDIA_COPY_PATHS = (
        {'from': os.path.join(CALLOWAY_ROOT, 'media'), 'to': STATIC_ROOT},
        {'from': 'static', 'to': STATIC_ROOT},
    )
    STATIC_MEDIA_COMPRESS_CSS = not DEBUG
    STATIC_MEDIA_COMPRESS_JS = not DEBUG
    STATIC_MEDIA_PURGE_OLD_FILES = False
    
The last bits you need to consider is middleware. Again here is an example of
``MIDDLEWARE_CLASSES`` that play nicely with Calloway::

    MIDDLEWARE_CLASSES = (
        'django.middleware.cache.UpdateCacheMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.middleware.gzip.GZipMiddleware',
        'django.middleware.http.ConditionalGetMiddleware',
        'django.middleware.doc.XViewMiddleware',
        'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
        'pagination.middleware.PaginationMiddleware',
        'django.middleware.transaction.TransactionMiddleware',
        'ban.middleware.DenyMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
    )


And finally there are some settings you could define in ``local_settings.py``
which should make life a bit easier including media::

    CACHE_BACKEND = "dummy:///"
    MEDIA_ROOT_PREFIX = 'media'
    MEDIA_URL_PREFIX = '/media/'
    MEDIA_ROOT = 'uploads'
    ADMIN_MEDIA_PREFIX = '/media/static/admin/'


URLs
-----

Now you can add the Calloway urlpatterns onto your existing patterns in ``urls.py``::

    from calloway.urls import urlpatterns as calloway_patterns

    urlpatterns += calloway_patterns

If you also want the catch all categories app to start at the site root, add this line::

    urlpatterns += patterns('', ('', include('categories.urls')))

Lastly you can setup a development media server to host your assets::

    if settings.DEBUG:
        urlpatterns += patterns('django.views.static',
            (r'^media/static/(?P<path>.*)$', 'serve',
                {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
        )


