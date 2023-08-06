#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name = 'sower_androidemu',
    version = '1.6',
    keywords='sower',
    description = 'sower',
    license = 'MIT License',
    url = 'https://github.com/',
    author = 'sower',
    author_email = 'nixingzhe5969@dingtalk.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [
        'unicorn==1.0.2',
        'capstone==4.0.1',
        'xmltodict>=0.11.0'
        ],
)