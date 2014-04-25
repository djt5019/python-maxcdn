#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys

install_requires = ['requests', 'requests_oauthlib', 'certifi']
tests_require = ['nose']

if sys.version_info < (3, 2, 0):
    tests_require.append('mock')

if sys.version_info < (2, 7, 0):
    tests_require.append('unittest2')


setup(
    name='maxcdn',
    version='0.0.3',
    description='A Python REST Client for MaxCDN REST Web Services',
    author='Joshua P. Mervine',
    author_email='joshua@mervine.net',
    license='MIT',
    keywords='MaxCDN CDN API REST',
    packages=find_packages(exclude=['tests', 'tests.*']),
    url='http://github.com/maxcdn/python-maxcdn',
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP'
        'Topic :: Software Development :: Libraries',
    ],
)
