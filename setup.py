#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='RLGames',
      version='0.1',
      description='Reinforcement Learning applied on environment developed with Pygame',
      url='http://github.com/MarcoFavorito/RLGames.git',
      author='Luca Iocchi',
      packages=find_packages(include=['RLGames*']),
      install_requires=["gym", "pygame"],
      zip_safe=False)