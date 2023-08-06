from setuptools import setup, find_packages

setup(
    name='vtpython',
    version='1',
    description='A very simple API to communicate with the VirusTotal V3 API',
    author='Mateo Mrvelj',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
