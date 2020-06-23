from setuptools import setup
import sys 
if sys.version_info < (3,0): 
    raise RuntimeError("This package requres Python 3.5+")

with open("README.md", 'r') as f: 
    long_description = f.read() 

version = '1.0.8'

import os
if os.name == 'nt':
    raise RuntimeError("This module is not currently supported on Windows...")
    setup(
        name='smartinput',
        version=version,
        python_requires='>=3',
        description='Much better implementation of the python input function, with hints and history support.',
        license="MIT",
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Shivam Saini',
        author_email='shivamsn97@gmail.com',
        url='https://github.com/shivamsn97/smartinput',
        packages=['smartinput'],
        install_requires=['colorama==0.4.3'],
        classifiers=[ 'Programming Language :: Python :: 3',
                  'Programming Language :: Python :: 3.5', 
                  'Programming Language :: Python :: 3.6',
                  'Programming Language :: Python :: 3.7',
                  'Programming Language :: Python :: 3.8'
                ]
        )
else:   
    setup(
        name='smartinput',
        version=version,
        python_requires='>=3',
        description='Much better implementation of the python input function, with hints and history support.',
        license="MIT",
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Shivam Saini',
        author_email='shivamsn97@gmail.com',
        url='https://github.com/shivamsn97/smartinput',
        packages=['smartinput'],
        install_requires=['colorama==0.4.3','getch==1.0'],
        classifiers=[ 'Programming Language :: Python :: 3',
                  'Programming Language :: Python :: 3.5', 
                  'Programming Language :: Python :: 3.6',
                  'Programming Language :: Python :: 3.7',
                  'Programming Language :: Python :: 3.8'
                ]
        )
