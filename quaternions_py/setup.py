# Import required functions
from setuptools import setup, find_packages

# Call setup function
setup(
    author='Dario Rodriguez',
    description='A simple package of quaternions algebra',
    name='quaternions_py',
    version='0.1.0',
    packages=find_packages('quaternions_py', 'quaternions.*'),
    install_requires=[
        'numpy',
        'math'
    ]
)