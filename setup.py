from setuptools import setup, find_packages
import os.path as op

packages = find_packages()

with open('requirements.txt') as rf:
    requirements = rf.readlines()

setup(name='neurodesign',
      version='0.2.2',
      description='Package for design optimisation for fMRI experiments',
      author='Joke Durnez',
      author_email='joke.durnez@gmail.com',
      license='MIT',
      packages=packages,
      install_requires=requirements,
      package_data={'neurodesign': [op.join('media', '*')]},
      zip_safe=False)
