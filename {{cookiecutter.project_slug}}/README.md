# {{cookiecutter.project_name}}

[`vpype`](https://github.com/abey79/vpype) plug-in to [_to be completed_]


## Examples

_to be completed_


## Installation

See the [installation instructions](https://vpype.readthedocs.io/en/latest/install.html) for information on how
to install `vpype`.


### Existing `vpype` installation

If *vpype* was installed using pipx, use the following command:

```bash
$ pipx inject vpype git+https://github.com/{{cookiecutter.author_github_id}}/{{cookiecutter.project_slug}}.
```

If *vpype* was installed using pip in a virtual environment, activate the virtual environment and use the following command:

```bash
$ pip install git+https://github.com/{{cookiecutter.author_github_id}}/{{cookiecutter.project_slug}}#egg={{cookiecutter.project_slug}}
```

Check that your install is successful:

```
$ vpype --help
Usage: vpype [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

Options:
  -v, --verbose
  -I, --include PATH  Load commands from a command file.
  --help              Show this message and exit.

Commands:
[...]
  Plugins:
    {{cookiecutter.command_name}}
[...]
```

### Stand-alone installation

Use this method if you need to edit this project. First, clone the project:

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
```

Check that your install is successful:

```
$ vpype --help
Usage: vpype [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

Options:
  -v, --verbose
  -I, --include PATH  Load commands from a command file.
  --help              Show this message and exit.

Commands:
[...]
  Plugins:
    {{cookiecutter.command_name}}
[...]
```


## Documentation

The complete plug-in documentation is available directly in the CLI help:

```bash
$ vpype {{cookiecutter.command_name}} --help
```


## License

See the [LICENSE](LICENSE) file for details.
