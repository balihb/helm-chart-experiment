import os

from setuptools import setup, find_packages

version_file = open(os.path.join('', 'VERSION'))

setup(
  name="example_server",
  version=version_file.read().strip(),
  install_requires=[
    'jsonpickle == 2.0.0'
  ],
  # packages=['example_server'],
  entry_points={
    "console_scripts": ["example-server=example_server.__main__:main"]
  },
  packages=find_packages(
    where='src'
  ),
  package_dir={"": "src"}
)
