from setuptools import setup, find_packages
import re
import os
from typing import List

HYPEN_DOT_E='-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    Read the requirements file and return a list of package names
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        for req in requirements:
           requirements= [req.replace("/n","")]
            
            
        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
    return requirements


setup(
    name='py_project',
    version='1.0',
    description='A simple Python project',
    author='Your Name',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )