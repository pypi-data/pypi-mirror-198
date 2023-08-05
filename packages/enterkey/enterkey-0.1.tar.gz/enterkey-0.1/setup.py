from setuptools import setup , find_packages

setup(
    name = 'enterkey',
    version = '0.1',
    author= 'Prince Kathuria',
    author_email='pk.kathuria9213@gmail.com',
    description='only enter key',
    packages=find_packages(),
    install_requires=[
    'Django>=3.0',
    ],
)