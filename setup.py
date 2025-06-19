from setuptools import setup, find_packages

setup(
    name='LegoTik',
    version='1.25.0',
    description='A simple and powerful library for FTP, networking, and file operations',
    author='KoldI (by: Xray4ik)',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'requests'
    ],
)
