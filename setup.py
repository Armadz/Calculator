from setuptools import setup, find_packages

setup(
    name='Calculator',
    version='0.1',
    packages=find_packages(),
    package_data={},
    scripts=[
        'bin/calculator.py',
    ],
)
