#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

required = ['stathat']

setup(
    name='stathat-async',
    version='0.0.1',
    description='A simple multiprocessing-based async API wrapper for StatHat.com',
    author='Jamie Matthews',
    author_email='jamie.matthews@gmail.com',
    url='https://github.com/j4mie/stathat-async',
    py_modules= ['stathatasync'],
    install_requires=required,
    license='MIT',
)
