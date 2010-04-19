import os, sys
from setuptools import setup


setup(
    name = "calloway",
    version = __import__('calloway').get_version().replace(' ', '-'),
    url = 'http://opensource.washingtontimes.com/projects/calloway/',
    author = 'The Washington Times Web Devs',
    author_email = 'webdev@washingtontimes.com',
    description = 'A news website builder from the Washington Times',
    packages = ['calloway'],
    include_package_data = True,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)


