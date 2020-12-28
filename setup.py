from setuptools import setup, find_packages


import datetime
import requests
import json

setup(
    name='Jsoneditoronline',
    version='1.0.0',
    url='https://github.com/raul27868/Jsoneditoronline.git',
    author='Raul Reyero',
    author_email='raul.reyero.diez@gmail.com',
    description='Api for https://jsoneditoronline.org',
    packages=find_packages(),    
    install_requires=['requests >= 1.0', 'datetime >= 1.0'  ],
)
 



