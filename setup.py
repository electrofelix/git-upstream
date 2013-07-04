#!/usr/bin/env python
#
# Copyright (c) 2012, 2013 Hewlett-Packard Development Company, L.P.
#
# Confidential computer software. Valid license from HP required for
# possession, use or copying. Consistent with FAR 12.211 and 12.212,
# Commercial Computer Software, Computer Software Documentation, and
# Technical Data for Commercial Items are licensed to the U.S. Government
# under vendor's standard commercial license.
#


import os
from setuptools import setup, find_packages
from ghp import version


# following function is taken from setuptools example.
# https://pypi.python.org/pypi/an_example_pypi_project (BSD)
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="hpgit",
    version=version.version,
    author="Darragh Bailey",
    author_email="dbailey@hp.com",
    description=("Tool supporting HPCloud git workflows."),
    license="Proprietary",
    keywords="git hpcloud workflow",
    url="https://wiki.hpcloud.net/display/auto/hpgit",
    scripts=['git-hp'],
    packages=find_packages(exclude=['test']),
    long_description=read('README'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: Other/Proprietary License",
    ],
)
