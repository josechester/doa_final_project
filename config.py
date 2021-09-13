#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Car_Module",
    version="1.0.4",
    author="Jose Martinez",
    description=("example of pytest with GitHub Actions"),
    license="GNU",
    keywords="example pytest",
    packages=['mean', 'tests', 'doc'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Test",
    ],
)
