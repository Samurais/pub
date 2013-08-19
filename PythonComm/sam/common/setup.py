'''
Created on Aug 15, 2013

@author: hailiang
'''
from setuptools import setup
from setuptools import find_packages

#TODO setup your env
setup(
      name="mytest",
      version="0.10",
      description="My test module",
      author="Robin Hood",
      url="http://www.csdn.net",
      license="LGPL",
      packages=find_packages(),
      scripts=["scripts/test.py"],
      )
