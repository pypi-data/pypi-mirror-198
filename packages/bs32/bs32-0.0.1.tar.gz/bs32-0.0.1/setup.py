import setuptools
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name='bs32',
    version='0.0.1',
    author='Mohammed Hamza',
    author_email='eibdhhs0@gmail.com',
    description='This Lebrary for Main Lebrary ccode',
    packages=setuptools.find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Natural Language :: Arabic',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License '
    ],
    install_requires=['pycryptodome']
)

