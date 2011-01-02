from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='evedb',
      version=version,
      description="A simple framework allowing you to export the eve public database to any sqlalchemy compatible datasource",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='John-John Tedro',
      author_email='johnjohn.tedro@gmail.com',
      url='http://toolchain.eu',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
            'evedb = evedb:entrypoint',
          ]
        }
      )
