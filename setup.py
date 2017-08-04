#-*-coding:utf8;-*-
#qpy:3
#qpy:console


"""A setuptools based setup module.

See:

https://packaging.python.org/en/latest/distributing.html

https://github.com/pypa/sampleproject

"""
# Always prefer setuptools over distutils

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))
print(path.join(here, 'README.rst'))
long_desc=open(path.join(here, 'README.rst'), encoding='utf-8').read()
print(long_desc)
packagelist = ['SameEndFinder','SameEndFinder.tests']

setup(
    name='SameEndFinder',
    version='0.0.1',
    description='a simple checker',
    long_description=long_desc,
    author='pjose',
    packages=packagelist,
    entry_points={
    	 'console_scripts':[
    	   'sameendfinder=SameEndFinder:main'
    	  ]
    	},

)