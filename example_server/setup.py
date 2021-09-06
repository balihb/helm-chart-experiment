import os

from setuptools import setup, find_packages
import os.path

version_file = open(os.path.join(
  os.path.abspath(os.path.dirname(__file__)),
  'VERSION'
))
version = version_file.read().strip()

setup(
  name="example_server",
  version=version,
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
