import os
from typing import List
from setuptools import find_packages,setup

hypen_e='-e .'
def get_requirements(file_name: str)->List[str]:
    """
    This function will return the list of python packages from requirements.txt file.
    """
    requirements=[]
    with open(file_name) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n'," ") for req in requirements]
        if hypen_e in requirements:
            requirements.remove(hypen_e)
    return requirements



setup(
    name='ml_project',
    version='0.0.1',
    author='Karan Mehta',
    author_email='kmehta883@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
