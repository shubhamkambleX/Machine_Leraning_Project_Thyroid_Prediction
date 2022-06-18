from pickle import LIST
from setuptools import setup
from typing import List


# Declaring the variables
Project_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR="SHubham Kamble"
DESCRIPTION = "Machine Learning Project"
PACAKGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    this is fucntion will return the list of requirements
    which is present in requirements.txt
    """
    with open(REQUIREMENT_FILE_NAME) as reqirements_file:
        return reqirements_file.readlines()

setup(
    name=Project_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACAKGES,
    install_requires=get_requirements_list()
)
