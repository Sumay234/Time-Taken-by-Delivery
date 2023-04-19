## Setup.py file is used for distribution 

## important liabaries for setup file
from setuptools import find_packages,setup
from typing import List

requirment_file_name='requirements.txt'
REMOVE_PACKAGE = "-e ."

def get_requirements() ->List[str]:
    with open(requirment_file_name) as requirement_file:
        requirment_list = requirement_file.readline()
    requirment_list = [requirement_name.replace("\n","") for requirement_name in requirment_list]
    
    if REMOVE_PACKAGE in requirment_list:
        requirment_list.remove(REMOVE_PACKAGE)
    return requirment_list


setup(name='Delivery_Time_Taken',
      version='1.0',
      description='Delivery Time Project :Domain - Food sector',
      author='Sumay Chatterjee',
      author_email='sumaykumar234@gmail.com',
      packages=find_packages(),  ## it will find all the folder or package which having __init__ file  to install 
      install_reqires=get_requirements()
     )
