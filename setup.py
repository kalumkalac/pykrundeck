#!/usr/bin/env python

from setuptools import setup, find_packages
import os
from pip.req import parse_requirements


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def requirements(requirements_file='requirements.txt'):
    reqs_from_file = parse_requirements(
        os.path.join(os.path.dirname(__file__), requirements_file),
        session=False
    )
    reqs = []
    for r in reqs_from_file:
        if r.req:
            reqs.append(str(r.req))
        # else:
        #     reqs.append(str(r.link))
    return reqs


setup(
    name='pykrundeck',
    version='0.92.1',
    description='Python REST API client for Rundeck 2.6+',
    long_description=read('README.md'),
    author='kalumkalac',
    author_email='delovan@gmail.com',
    url='https://github.com/kalumkalac/pyrundeck',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements(),
)
