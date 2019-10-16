from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dekit',
    version='0.0.1',
    description='A collection of useful Python decorators',
    long_description=readme,
    author='Kaitian Xie',
    author_email='xkaitian@gmail.com',
    url='https://github.com/algobot76/dekit',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
