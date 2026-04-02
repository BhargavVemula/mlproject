from setuptools import setup,find_packages
from typing import List

HYPEN_DOT_E = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    this function will ruturn requirements
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readline()
        requirements = [req.replace("/n","") for req in requirements]
    
    if HYPEN_DOT_E in requirements:
        requirements.remove(HYPEN_DOT_E)
    
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Bhargav",
    author_email="vbnbhargav@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)