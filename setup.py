import os, sys
from setuptools import setup, find_packages

def read_file(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except:
        return ''
r =  [x for x in read_file('setup/requirements.txt').splitlines() if not x.lstrip().startswith('#') and x]

setup(
    name = "calloway",
    version = __import__('calloway').get_version().replace(' ', '-'),
    url = 'http://opensource.washingtontimes.com/projects/calloway/',
    author = 'The Washington Times Web Devs',
    author_email = 'webdev@washingtontimes.com',
    description = 'A website builder from the Washington Times',
    long_description = read_file('README'),
    scripts = ['setup/calloway.py'],
    packages = find_packages(),
    include_package_data = True,
    install_requires =r,
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


