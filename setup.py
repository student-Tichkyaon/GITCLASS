from setuptools import find_packages,setup
# from typing import List


def get_requirements()->list[str]:

    reuirements_list  = list[str]= []
    return reuirements_list

setup(
    name='sensor',
    version="0.0.1",
    author="Tisha",
    author_email="photo08upload200527@gmail.com",
    packages=find_packages(),
    install_requires =  get_requirements , #["pymongo"],
)