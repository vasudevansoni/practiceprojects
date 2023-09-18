from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_require_install(filepath:str)->List[str]:
    requirements = []

    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="practice machine learning project end to end",
    author="vasudevan",
    author_email="vasudevansoni07@gmail.com",
    version="0.0.1",
    install=get_require_install('requirements.txt')
)