#!/usr/bin/env python
# coding: utf-8
from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = ""

setup(
    name='example_package',
    version='0.0.1',
    description='Demo',
    author='SolarisNeko',
    author_email='1417015340@qq.com',
    url='https://github.com/SolarisNeko/python-try-to-upload-pypi',
    packages=['src'],
    install_requires=['six>=1.12.0'],
    keywords='demo',
    long_description=long_description,
    python_requires=">=3.7"
)
