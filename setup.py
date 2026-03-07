from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
        this function will return the list of requirements
    """
    with open(file_path,'r') as file:
        reqs = [line.strip() for line in file]
        if(HYPHEN_E_DOT in reqs):
            reqs.remove(HYPHEN_E_DOT)
        return reqs
    

print(get_requirements("requirements.txt"))

setup(
    name="ml-project",
    author="Hazem Emam",
    author_email="hemam8560@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt"),
)