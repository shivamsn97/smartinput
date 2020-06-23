from setuptools import setup

with open("README.md", 'r') as f: 
    long_description = f.read() 

setup(
    name='smartinput',
    version='0.1.6',
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
                  'Programming Language :: Python :: 3.6'
                ]
)
