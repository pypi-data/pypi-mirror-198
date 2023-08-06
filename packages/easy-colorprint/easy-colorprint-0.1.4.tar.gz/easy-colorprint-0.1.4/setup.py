from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='easy-colorprint',
    version='0.1.4',
    description='Une librairie pour imprimer en couleur à l\'écran',
    author='Romain Dudek',
    packages=find_packages(),
    install_requires=[
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/romaindudek/colorPrint'
)