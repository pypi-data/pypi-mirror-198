from setuptools import setup, find_packages
import os
from pathlib import Path

setup(
    name='JohnServerAPI',
    version='0.0.2',
    description='This is a module to interact with Server and Client',
    author='John',
    author_email='myemail@example.com',
    install_requires=[
        'requests',
        'numpy',
        'matplotlib',
        'ipaddress',
    ],
    packages=find_packages(include=["JohnServerAPI", "test_johnserverapi"]),
   long_description=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ReadMe.md")).read(),
    long_description_content_type="text/markdown",
)
