from setuptools import setup


with open("README.md") as f:
    readme = f.read()

setup(
    name="{{cookiecutter.project_slug}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.project_description}}",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author_name}}",
    url="https://github.com/{{cookiecutter.author_github_id}}/{{cookiecutter.project_slug}}",
    packages=["{{cookiecutter.project_identifier}}"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Topic :: Multimedia :: Graphics",
        "Environment :: Plugins",
    ],
    setup_requires=["wheel"],
    install_requires=[
        'click',
        'vpype[all]>=1.10,<2.0',
    ],
    entry_points='''
            [vpype.plugins]
            {{cookiecutter.command_name}}={{cookiecutter.project_identifier}}.{{cookiecutter.command_name}}:{{cookiecutter.command_name}}
        ''',
)
