from setuptools import setup


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="{{cookiecutter.project_slug}}",
    version="{{cookiecutter.version}}",
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author_name}}",
    url="",
    license=license,
    packages=["{{project_identifier}}"],
    install_requires=[
        'click',
        'vpype @ git+https://github.com/abey79/vpype.git',
    ],
    entry_points='''
            [vpype.plugins]
            {{cookiecutter.command_name}}={{cookiecutter.project_identifier}}.{{cookiecutter.command_name}}:{{cookiecutter.command_name}}
        ''',
)
