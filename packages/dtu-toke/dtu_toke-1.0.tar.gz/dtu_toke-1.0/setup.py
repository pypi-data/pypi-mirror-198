
from setuptools import setup

# Read contents of the README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='dtu_toke',
      version='1.0',
      description='My first package',
      long_description = 'Testing my first package',
      author='toke.schaffer',
      packages=['dtu_toke'],
     )
