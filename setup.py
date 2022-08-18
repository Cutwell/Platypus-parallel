#!/usr/bin/env python

from setuptools import setup

setup(name='Platypus-Opt-Parallel',
      version='0.0.1', # Update __init__.py if the version changes!
      description='Async Multiobjective optimization in Python',
      author='David Hadka, Zachary Smith',
      author_email='zachsmith.dev@gmail.com',
      license="GNU GPL version 3",
      url='https://github.com/Cutwell/Platypus-parallel',
      packages=['platypus'],
      install_requires=['six'],
      tests_require=['pytest', 'mock'],
      python_requires='>=3.6'
     )
