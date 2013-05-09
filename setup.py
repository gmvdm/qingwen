#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2012 Geoff Wilson

from setuptools import setup, find_packages


setup(name='qingwen',
      description='Process data from the Qingwen iOS dictionary',
      author='Geoff Wilson',
      author_email='gmwils@gmail.com',
      version='0.1',
      packages=find_packages(),
      scripts=['bin/qingwen'],
      license = 'MIT',
      )
