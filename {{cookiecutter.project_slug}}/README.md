# {{cookiecutter.project_name}}

[`vpype`](https://github.com/abey79/vpype) plug-in to [_to be completed_]


## Examples

_to be completed_


## Installation

See the [installation instructions](https://vpype.readthedocs.io/en/latest/install.html) for information on how
to install `vpype`.

If *vpype* was installed using pipx, use the following command:

```bash
$ pipx inject vpype {{cookiecutter.project_slug}}
```

If *vpype* was installed using pip in a virtual environment, activate the virtual environment and use the following command:

```bash
$ pip install {{cookiecutter.project_slug}}
```

Check that your install is successful:

```
$ vpype {{cookiecutter.command_name}} --help
[...]
```

## Documentation

The complete plug-in documentation is available directly in the CLI help:

```bash
$ vpype {{cookiecutter.command_name}} --help
```


## Development setup

Here is how to clone the project for development:

```bash
$ git clone https://github.com/{{cookiecutter.author_github_id}}/{{cookiecutter.project_slug}}.git
$ cd {{cookiecutter.project_slug}}
```

Create a virtual environment:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
```

Install `{{cookiecutter.project_slug}}` and its dependencies (including `vpype`):

```bash
$ pip install -e .
$ pip install -r dev-dependencies.txt
```


## License

See the [LICENSE](LICENSE) file for details.
