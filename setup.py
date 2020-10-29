import setuptools
from setuptools import setup

setup(
    name='biograder',
    version='0.0.1',
    author='PayneLab',
    description='grader',
    url='https://github.com/PayneLab/biograder',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)