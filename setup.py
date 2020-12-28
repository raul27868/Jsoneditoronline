from setuptools import setup, find_packages


import datetime
import requests
import json

setup(
    name='MyUtilities',
    version='1.0.0',
    url='https://github.com/raul27868/MyUtilities.git',
    author='Raul Reyero',
    author_email='raul.reyero.diez@gmail.com',
    description='Multiples utilities',
    packages=find_packages(),    
    install_requires=[ 'simplejson'  ],
)
 



