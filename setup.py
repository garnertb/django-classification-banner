#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import re
import os
from setuptools import find_packages


name = 'django-classification-banner'
package = 'django_classification_banner'
description = 'A django app that adds classification banners to your site.'
url = 'https://github.com/garnertb/django-classification-banner'
author = 'Tyler Garner'
author_email = 'garnertb@gmail.com'
license = 'MIT'
install_requires = []


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name=name,
    version=get_version(package),
    url=url,
    license=license,
    description=description,
    author=author,
    author_email=author_email,
    packages= find_packages(exclude=["tests.*", "tests"]),
    package_data=get_package_data(package),
    install_requires=install_requires,
    zip_safe=False
)