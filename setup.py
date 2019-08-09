#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
  name='dashformation',
  version='1.0.0',
  license='MIT',
  description='Python library for generating AWS CloudWatch dashboards',
  author='Adam Miller',
  author_email='miller@adammiller.io',
  url='https://github.com/adammillerio/dashformation',
  download_url='https://github.com/adammillerio/dashformation/archive/v1.0.0.tar.gz',
  keywords=[],
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3 :: Only',
  ],
  packages=find_packages(),
  include_package_data=True
)
