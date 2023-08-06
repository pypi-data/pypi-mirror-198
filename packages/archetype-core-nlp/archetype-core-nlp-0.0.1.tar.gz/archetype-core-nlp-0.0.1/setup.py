#! /usr/bin/env python3
import os

from setuptools import setup, find_namespace_packages

PROJECT_DIR = os.path.dirname(__file__)

INFO = open(os.path.join(PROJECT_DIR, 'INFO')).readlines()
INFO = dict((l.strip().split('=') for l in INFO))

DEPENDENCIES = open(os.path.join(PROJECT_DIR, 'requirements.txt')).readlines()

setup(name='archetype-core-nlp',
      version=INFO['version'],
      author=INFO['author'],
      author_email=INFO['author_email'],
      url=INFO['url'],
      python_requires='>=3.8',
      entry_points={
          'console_scripts': ['core=infra.core.forge:main']
      },
      packages=find_namespace_packages(include=['infra.core.forge','infra.core.forge.*']),
      namespace_packages=['infra', 'infra.core'],
      install_requires=[d for d in DEPENDENCIES if '://' not in d],
      package_data={'infra.core.forge': ['templates/*']},
      zip_safe=False)
