import os
import sys
from setuptools import setup

# Add pypertext directory with version.py to the path.
sys.path.append(os.path.join(os.getcwd(), "pypertext"))

from version import __version__  # type: ignore

setup(version=__version__)
