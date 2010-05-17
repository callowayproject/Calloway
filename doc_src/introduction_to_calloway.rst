
========================
Introduction to Calloway
========================

Calloway was dreamed up to be a fast way to get a web site going. Most web sites have an infrastructure that is painful to recreate each time. Our goal is to allow programmers to specify the functionality they want included, and then focus on the parts that make their website unique.

The underlying framework upon which Calloway resides is Django. It is written in Python and promotes adding functionality in "Applications" that can be reused in other projects. This isolation of functionality is what Calloway uses to combine other open source projects together to create a cohesive infrastructure.

What Calloway Provides
======================

* Static media minification and migration to a separate media server

* IP address banning

* Use cookies for session identification

* Allow case-insensitive user login using a uesrname or e-mail address

* Multi-media asset management

* Customized admin with dashboard

* A versioned cache for allowing for website and other updates

* Staff profile management

* Stories with revision control and site-positioning

* Hierarchical categorization

* Threaded commenting with moderation

* Polls

* Multi-user blogs

* Robots.txt management

* Easy template tag creation library

* Hierarchical navigation menu

* Google Analytics management

* Voting

* Sharing

* User registration


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

