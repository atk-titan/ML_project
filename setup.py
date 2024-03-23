from setuptools import setup, find_packages

def read_requirements(filename):
    """Reads requirements from a file."""
    requirements=[]
    with open(filename, 'r') as f:
        requirements = f.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if '-e.' in requirements:
            requirements.remove('-e.')
    return requirements

setup(
    name="First_project",
    version='0.0.1',
    author='Gaurav',
    author_email='gauravmane8451@gmail.com',
    packages=find_packages(),
    requires=read_requirements('requirements.txt') ,  # Use install_requires for dependencies
)
