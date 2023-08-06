#
# Filename: setup.py
#
# Author: Simon Redman <simon@ergotech.com>
# File Created: 05.03.2023
# Last Modified: Wed 08 Mar 2023 09:17:38 PM EST
# Description: 
#
#

from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='suta_bed',
    version='0.1.4',
    license='MIT',
    author="Simon Redman",
    author_email='simon@ergotech.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages('suta_bed'),
    package_dir={'': 'suta_bed'},
    url='https://github.com/sredman/suta-ble-bed',
    keywords=['SUTA','sleepmotion','i500','i900','i200'],
)
