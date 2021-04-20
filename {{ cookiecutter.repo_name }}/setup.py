from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.repo_name }}',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='Department of Social Protection',
    license='EUPL',
)
