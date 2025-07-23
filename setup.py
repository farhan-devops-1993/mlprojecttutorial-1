# Importing the setup() function and find_packages() helper from setuptools
# setup() is used to configure the package details
# find_packages() automatically finds all sub-packages to include in the distribution
from setuptools import find_packages, setup

# Importing List type hint from the typing module
# This allows us to specify that a function will return a list of strings
from typing import List
HYPEN_E_DOT='-e .'

# Define a function to read the requirements from a given file
# It takes the path to the requirements file and returns a list of package names
def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads a requirements.txt file and returns
    a cleaned list of required packages (without newline characters).
    '''
    # Initialize an empty list to store the requirements
    requirements = []

    # Open the file at the given path in read mode
    with open(file_path) as file_obj:
        # Read all lines from the file into a list
        # Each line typically contains one package (e.g., numpy\n)
        requirements = file_obj.readlines()

        # Remove newline characters from each requirement line
        # Using list comprehension to clean all lines
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    # Return the cleaned list of requirements
    return requirements

# Call the setup() function to define the package metadata and configuration
setup(
    name='mlproject',  # Name of the project/package
    version='0.0.03',  # Version of the project
    author='farhan'
    author_email='farhan@gmail.com',  # Email of the project author or maintainer
    packages=find_packages(where='src'),  # Automatically find and include all packages in the project directory
    #package_dir={'': 'src'},  # Map root (empty string) to 'src' directory
    install_requires=get_requirements('requirements.txt')  # Install dependencies listed in requirements.txt
)
