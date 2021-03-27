"""Setup.py entry point for package.

Configuration is handled by setuptools>30.3.0 through setup.cfg.
https://setuptools.readthedocs.io/en/latest/setuptools.html#metadata
https://setuptools.readthedocs.io/en/latest/setuptools.html#options
"""

import setuptools
from setuptools import setup, find_packages

setuptools.setup(
    name='saml2',
    #package_dir={'': 'src'},
    packages=find_packages(),
    version='5.1.0'
)
