===============================
Application bundles in settings
===============================

Calloway's settings includes bundles of applications that are either dependent upon each other, or work well together. Some application bundles have suggestions for others that can augment their functionality, but are not required.



Application bundles are only for convenience. Feel free to mix and match applications.



``calloway.settings.APPS_CORE``
===============================

These applications are considered core to any project and consist of Django ``contrib`` applictions.


Suggested application bundles: ``APPS_TINYMCE``\ , ``APPS_REVERSION`` (for flatpages)


* ``django.contrib.auth``
* ``django.contrib.contenttypes``
* ``django.contrib.sessions``
* ``django.contrib.sites``
* ``django.contrib.flatpages``
* ``django.contrib.humanize``
* ``django.contrib.comments``
* ``django.contrib.markup``
* ``django.contrib.redirects``



.. _apps_admin:

``calloway.settings.APPS_ADMIN``
================================

The admin area of the project requires several apps. The ``livevalidation`` application provides real-time validation of forms, including the admin forms. ``django-admin-tools`` provides the custom skin.

* `livevalidation <http://opensource.washingtontimes.com/projects/django-livevalidation/>`_
* `admin_tools <http://bitbucket.org/izi/django-admin-tools/wiki/Home>`_
* `admin_tools.theming <http://bitbucket.org/izi/django-admin-tools/wiki/Home>`_
* `admin_tools.menu <http://bitbucket.org/izi/django-admin-tools/wiki/Home>`_
* `admin_tools.dashboard <http://bitbucket.org/izi/django-admin-tools/wiki/Home>`_
* ``django.contrib.admin``


.. _apps_calloway_default:

``calloway.settings.APPS_CALLOWAY_DEFAULT``
===========================================

Calloway includes no real applications, except ``django_ext`` which are small extensions to Django. Various utilities are included within this, including a case-insensitive authorization, requirements generator and a few others.

* ``django_ext``


.. _apps_mptt:

``calloway.settings.APPS_MPTT``
===============================

Django MPTT is an application that enhances other applications' ability to manage hierarchical data. It is required in :ref:`APPS_CATEGORIES <apps_categories>` and :ref:`APPS_COMMENT_UTILS <apps_comment_utils>`\ .

We specify an updated and Django 1.x compatible version named `django-mptt-2 <http://github.com/batiste/django-mptt>`_\ .


* `mptt <http://github.com/batiste/django-mptt>`_


.. _apps_staff:

``calloway.settings.APPS_STAFF``
================================

A specialized profile for staff members.


Suggested application bundles: :ref:`APPS_TINYMCE <apps_tinymce>`

* `staff <http://opensource.washingtontimes.com/projects/django-staff/>`_


.. _apps_reversion:

``calloway.settings.APPS_REVERSION``
====================================

Django Reversion is an app that enhances other applications. It allows you to view and revert to previous versions of records. Django Stories and Django Flatpages are currently configured to use it.


* `reversion <http://code.google.com/p/django-reversion/>`_



.. _apps_stories:

``calloway.settings.APPS_STORIES``
==================================

A bundle of applications for creating news.

Suggested application bundles: :ref:`APPS_TINYMCE <apps_tinymce>`\ , :ref:`APPS_REVERSION <apps_reversion>`


* `stories <http://opensource.washingtontimes.com/projects/django-stories/>`_
* `positions <http://opensource.washingtontimes.com/projects/django-kamasutra/>`_
* `news_sitemaps <http://opensource.washingtontimes.com/projects/django-news-sitemaps/>`_
* `viewpoint <http://opensource.washingtontimes.com/projects/viewpoint/>`_
* `pullquote <http://opensource.washingtontimes.com/projects/pullquote/>`_



.. _apps_categories:

``calloway.settings.APPS_CATEGORIES``
=====================================

A hierarchical category manager. Requires ``:ref:`APPS_MPTT <apps_mptt>```.

* `categories <http://opensource.washingtontimes.com/projects/django-categories/>`_
* `editor <http://opensource.washingtontimes.com/projects/django-categories/>`_


.. _apps_comment_utils:

``calloway.settings.APPS_COMMENT_UTILS``
========================================

Utilities for adding threaded comments to the default Django comments app and management of offensive comments. Requires :ref:`APPS_MPTT <apps_mptt>`


* `mptt_comments <http://bitbucket.org/justquick/django-mptt-comments>`_
* `offensivecontent <http://opensource.washingtontimes.com/projects/offensivecontent/>`_


.. _apps_frontend_admin:

``calloway.settings.APPS_FRONTEND_ADMIN``
=========================================

Allows using your admin forms in a regular template. Requires livevalidation in :ref:`APPS_ADMIN <apps_admin>`\ .

* `frontendadmin <http://github.com/bartTC/django-frontendadmin>`_

.. _apps_media:

``calloway.settings.APPS_MEDIA``
================================


* `massmedia <http://opensource.washingtontimes.com/projects/massmedia/>`_
* `tagging <http://code.google.com/p/django-tagging/>`_
* `staticmediamgr <http://opensource.washingtontimes.com/projects/django-staticmediamgr/>`_



.. _apps_utils:

``calloway.settings.APPS_UTILS``
================================

* `robots <http://bitbucket.org/jezdez/django-robots/>`_
* `piston <http://bitbucket.org/jespern/django-piston/wiki/Home>`_
* ``ban``
* ``native_tags``
* ``google_analytics``
* ``hiermenu``
* ``synagg``
* `uni_form <http://github.com/pydanny/django-uni-form>`_
* `critic <http://opensource.washingtontimes.com/projects/critic/>`_
* ``mailfriend``
* `debug_toolbar <http://github.com/robhudson/django-debug-toolbar>`_
* `pollit <http://opensource.washingtontimes.com/projects/pollit/>`_



.. _apps_caching:

``calloway.settings.APPS_CACHING``
==============================================================

* `django_memcached <http://github.com/ericflo/django-memcached>`_
* `versionedcache <http://github.com/ella/django-versionedcache>`_



.. _apps_registration:

``calloway.settings.APPS_REGISTRATION``
=======================================

* ``registration``
* ``custom_registration``



.. _apps_tinymce:

``calloway.settings.APPS_TINYMCE``
==================================

* `tinymce <http://code.google.com/p/django-tinymce/>`_

