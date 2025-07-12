from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e."
def get_requirements(file_path:str) ->List[str]:
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = {req.replace ("\n", "") for req in requirements }

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements # type: ignore

setup(
name = 'MLProject',
version = '0.0.1',
author='Ashish',
author_email='ap69985@gmail.com',
packages=find_packages(),
install_requires=['pandas','numpy','seaborn']
)