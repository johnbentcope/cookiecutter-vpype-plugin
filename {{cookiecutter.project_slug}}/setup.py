from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="{{cookiecutter.project_name}}",
    version="{{cookiecutter.version}}",
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author_name}}",
    url="",
    license=license,
    packages=find_packages(exclude=("examples", "tests")),
    install_requires=[
        'click',
        'vpype @ git+https://github.com/abey79/vpype.git@feature-plugins',
    ],
    entry_points='''
            [vpype.plugins]
            {{cookiecutter.command_name}}={{cookiecutter.project_identifier}}.{{cookiecutter.project_identifier}}:{{cookiecutter.project_identifier}}
        ''',,
)
