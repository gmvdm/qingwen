#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


packages = [
    'qingwen',
    ]


requires = []


setup(name='qingwen',
      description='Process data from the Qingwen iOS dictionary',
      author='Geoff Wilson',
      author_email='gmwils@gmail.com',
      version='0.1',
      packages=packages,
      install_requires=requires,
      scripts=['bin/qingwen'],
      license = 'MIT',
      )
