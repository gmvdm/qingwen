#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2012 Geoff Wilson

from distutils.core import setup


setup(name='qingwen',
      description='Process data from the Qingwen iOS dictionary',
      author='Geoff Wilson',
      author_email='gmwils@gmail.com',
      version='0.1',
      packages=['qingwen'],
      scripts=['bin/qingwen'],
      )
