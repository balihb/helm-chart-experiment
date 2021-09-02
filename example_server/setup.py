from setuptools import setup

setup(
  name="example_server",
  install_requires=[
    'jsonpickle == 2.0.0'
  ],
  packages=['example_server'],
  entry_points={
    "console_scripts": ["example-server=example_server.__main__:main"]
  }
)
