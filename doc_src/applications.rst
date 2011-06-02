.. _application_bundles_in_settings:

===============================
Application bundles in settings
===============================

Calloway's settings includes bundles of applications that are either dependent upon each other, or work well together. Some application bundles have suggestions for others that can augment their functionality, but are not required.



Application bundles are only for convenience. Feel free to mix and match applications.



``calloway.settings.APPS_CORE``
===============================

.. warning::
   As of version 0.4 this application bundle is deprecated. In order to better handle core Django apps in different versions, this bundle has been broken into :ref:`apps_django_base`\ , :ref:`apps_django13_base`\ , and :ref:`apps_django_template_utils`\ .

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

.. _apps_django_base:

``calloway.settings.APPS_DJANGO_BASE``
======================================

.. note:: New in version 0.4

These are the core contrib apps included in the default settings for Django 1.0 - 1.2.

Suggested application bundles: ``APPS_TINYMCE``\ , ``APPS_REVERSION`` (for flatpages)

* ``django.contrib.auth``
* ``django.contrib.contenttypes``
* ``django.contrib.sessions``
* ``django.contrib.sites``
* ``django.contrib.flatpages``

.. _apps_django13_base:

``calloway.settings.APPS_DJANGO13_BASE``
========================================

.. note:: New in version 0.4

These are the core contrib apps included in the default settings for Django 1.3.

Suggested application bundles: ``APPS_TINYMCE``\ , ``APPS_REVERSION`` (for flatpages)

* ``django.contrib.auth``
* ``django.contrib.contenttypes``
* ``django.contrib.sessions``
* ``django.contrib.sites``
* ``django.contrib.flatpages``
* ``django.contrib.messages``
* ``django.contrib.staticfiles``

.. _apps_django_template_utils:

``calloway.settings.APPS_DJANGO_TEMPLATE_UTILS``
================================================

.. note:: New in version 0.4

When you want special help with templates, these contrib apps can help out.

* ``django.contrib.humanize``
* ``django.contrib.markup``
* ``django.contrib.webdesign``

.. _apps_admin:

``calloway.settings.APPS_ADMIN``
================================

The admin area of the project requires several apps. The ``livevalidation`` application provides real-time validation of forms, including the admin forms. ``django-admin-tools`` provides the custom skin.

.. warning::
   In version 0.4, livevalidation has been removed from this bundle.

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

* `mptt <https://github.com/django-mptt/django-mptt>`_


.. _apps_staff:

``calloway.settings.APPS_STAFF``
================================

A specialized profile for staff members.


Suggested application bundles: :ref:`APPS_TINYMCE <apps_tinymce>`

* `staff <https://github.com/callowayproject/django-staff>`_


.. _apps_reversion:

``calloway.settings.APPS_REVERSION``
====================================

Django Reversion is an app that enhances other applications. It allows you to view and revert to previous versions of records. Django Stories and Django Flatpages are currently configured to use it.


* `reversion <http://code.google.com/p/django-reversion/>`_



.. _apps_stories:

``calloway.settings.APPS_STORIES``
==================================

.. warning:: 
   Changed in version 0.4: Django Viewpoint (a blogging app) and Django Pullquote (for storing quotations) were removed.

A bundle of applications for creating news.

Suggested application bundles: :ref:`APPS_TINYMCE <apps_tinymce>`\ , :ref:`APPS_REVERSION <apps_reversion>`


* `stories <https://github.com/callowayproject/django-stories>`_
* `positions <https://github.com/callowayproject/django-kamasutra>`_
* `news_sitemaps <https://github.com/callowayproject/django-news-sitemaps>`_

.. _apps_blogging:

``calloway.settings.APPS_BLOGGING``
===================================

.. note:: New in version 0.4

A blogging platform for one blog or many blogs.

Suggested application bundles: :ref:`APPS_TINYMCE <apps_tinymce>`\ , :ref:`APPS_REVERSION <apps_reversion>`

* `viewpoint <https://github.com/callowayproject/django-viewpoint>`_


.. _apps_categories:

``calloway.settings.APPS_CATEGORIES``
=====================================

A hierarchical category manager. Requires ``:ref:`APPS_MPTT <apps_mptt>```.

* `categories <https://github.com/callowayproject/django-categories>`_
* `editor <https://github.com/callowayproject/django-categories>`_


.. _apps_comment_utils:

``calloway.settings.APPS_COMMENT_UTILS``
========================================

Utilities for adding threaded comments to the default Django comments app and management of offensive comments. Requires :ref:`APPS_MPTT <apps_mptt>`


* `mptt_comments <http://bitbucket.org/justquick/django-mptt-comments>`_
* `offensivecontent <https://github.com/callowayproject/django-offensivecontent>`_


.. _apps_frontend_admin:

``calloway.settings.APPS_FRONTEND_ADMIN``
=========================================

Allows using your admin forms in a regular template. Requires livevalidation in :ref:`APPS_ADMIN <apps_admin>`\ .

* `frontendadmin <http://github.com/bartTC/django-frontendadmin>`_

.. _apps_media:

``calloway.settings.APPS_MEDIA``
================================

.. warning:: 
   Changed in version 0.4: Django Tagging was moved to :ref:`apps_tagging`.

* `massmedia <https://github.com/callowayproject/django-massmedia>`_

.. _apps_tagging:

``calloway.settings.APPS_TAGGING``
* `tagging <http://code.google.com/p/django-tagging/>`_

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
* `critic <https://github.com/callowayproject/django-critic>`_
* ``mailfriend``
* `debug_toolbar <http://github.com/robhudson/django-debug-toolbar>`_
* `pollit <https://github.com/callowayproject/django-pollit>`_
* `pullquote <https://github.com/callowayproject/django-pullquote>`_



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

* `tinymce <https://github.com/justquick/django-tinymce>`_

