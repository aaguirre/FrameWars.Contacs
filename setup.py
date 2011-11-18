import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'pymongo',
    'wtforms',
    'pyramid_jinja2',
    ]

if sys.version_info[:3] < (2,5,0):
    requires.append('pysqlite')

setup(name='Contacts',
      version='0.0',
      description='Contacts',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='contacts',
      install_requires = requires,
      entry_points = """\
      [paste.app_factory]
      main = contacts:main
      """,
      paster_plugins=['pyramid'],
      )

