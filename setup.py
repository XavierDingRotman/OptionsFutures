from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='OptionsFutures',
    version='1.0.2',
    packages=find_packages(exclude=['test', 'data', 'analysis']),
    long_description=long_description,
    url='https://github.com/XavierDingRotman/OptionsFutures',
    license='Apache License 2.0',
    author='Xavier Ding',
    author_email='xavier.ding@rotman.utoronto.ca',
    description='An evaluation tool for options and futures'
)
