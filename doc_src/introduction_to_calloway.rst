
========================
Introduction to Calloway
========================

The underlying framework upon which Calloway resides is Django. It is written in Python and promotes adding functionality in pluggable "Applications" that can be reused in other projects. This isolation of functionality is what Calloway uses to combine other open source projects together to create a cohesive infrastructure.

Design Principles
=================

Calloway is based on four principles:

* **Integration without dependency** Django pluggable apps should do one thing and only one thing and do it well. For example, a blog app, should not include tagging, categories, authors, and other things that might augment the core functionality of the blog. It should manage blogs and entries and make it easy to write them and deliver them.
  
  This allows you to build the core infrastructure like building blocks, adding in the functionality that you need in the way you need it.

* **User interface for content managers is important** The Django admin has spoiled us developers. While it is great in many respects, where it is lacking is often overlooked by developers. The content managers, the ones who keep your site up-to-date with the stuff users want, suffer.
  
  We want to promote and provide methods to improve the user experience for content managers, and promote applications that do so as well.

* **Easy customization through overrides and fallbacks** The methods that Django uses for handling settings and templates nails this idea. Templates are easily overridden one at a time, and it is easy to provide template to fallback on if no other is there.

* **Simple enough for a designer to do it** This is not meant to be derogatory, but a workflow advantage. A designer that is comfortable with the command line should be able to bootstrap a project, pick the building blocks of functionality and start designing the front end.

Don't Assume. It makes an ass out of you ... and someone else
=============================================================

We've been frustrated attempting to get supposed "pluggable" applications to work together; even our own. We realized that most of the time, it is because the application was written with some assumptions that are either not communicated, or don't work in a different situation.

Calloway aims to be assumption free. But it probably isn't right now. That's because *you* haven't tried it in *your* situation to discover an assumption not yet realized and fixed.

What Calloway Provides
======================

* **Lists of application "bundles" that are known to work together.** Some of them we've written, most are really good third-party applications from the community. The application bundles are merely shortcuts and not required.
  
  You can see the list of application bundles at :ref:`application_bundles_in_settings`\ .

* **Dependency management.** With the applications that it knows about, it can generate a requirements file for ``pip`` to make installation of the packages easy.

* **Project templating.** The Django ``startproject`` command is nice for beginners, but is missing many things that you probably need and want. We provide an example project template, but encourage you to customize it to your heart's desire.

Structure of a Calloway Project
===============================

A fundamental Calloway principle is progressive enhancement. By providing good defaults, you only override what you need. You have access to individual parts, as well as a combined whole.


1. You create a project using a project template.

   * A project template is included, but you can modify it to your defaults

   * A script is used to walk you through the creation of the project

2. Your project includes Calloway as a dependency (that is typically defined already in the template project).

3. The ``settings.py`` in your project brings in Calloway's default settings, and specifies preset application bundles. Other applications or overrides of the defaults are also specified.

4. The ``urls.py`` in your project brings in Calloway's default routing, and overrides are added as necessary.

5. The template project includes common server configurations, customized by the ``create_project`` script.

