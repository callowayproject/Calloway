import os, sys
from setuptools import setup, find_packages

def read_file(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except:
        return ''

setup(
    name = "calloway",
    version = __import__('calloway').get_version().replace(' ', '-'),
    url = 'http://opensource.washingtontimes.com/projects/calloway/',
    author = 'The Washington Times Web Devs',
    author_email = 'webdev@washingtontimes.com',
    description = 'A builder of boring stuff for opinionated developers',
    long_description = read_file('README'),
    packages = find_packages(),
    include_package_data = True,
    
    
    scripts = ['calloway/bin/generate_reqs','calloway/bin/check_for_updates'],
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


