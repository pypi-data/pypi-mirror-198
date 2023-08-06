# ds-reify

[![Tests](https://github.com/gnodar01/ds-reify/workflows/Tests/badge.svg)](https://github.com/gnodar01/ds-reify/actions?workflow=Tests)
[![PyPI](https://img.shields.io/pypi/v/ds-reify.svg)](https://pypi.org/project/ds-reify/)

A CLI helper tool for [Distributed-Something](https://distributedscience.github.io/Distributed-Something/introduction.html)

## Development

### Setup Virtual Environment

Setup a python environment using the method of your choice.

Using the builtin `venv`:

    python -m venv <ENV_NAME>
    source <ENV_NAME>/bin/activate

Using `conda` (replace with any `python >= 3.8`):

    conda create -n <ENV_NAME> python=3.8
    conda activate <ENV_NAME>

Using whatever else you want, like [pyenv](https://github.com/pyenv/pyenv).

### Install dev tools

Install [Poetry](https://python-poetry.org/)

    curl -sSL https://install.python-poetry.org/ | python
    source ~/.poetry/env

Install [Nox](https://nox.thea.codes/en/stable/)

    pip install --user --upgrade nox

See [this post](https://medium.com/@cjolowicz/nox-is-a-part-of-your-global-developer-environment-like-poetry-pre-commit-pyenv-or-pipx-1cdeba9198bd) if you're curious as to why we don't install nox via Poetry.

Install [pre-commit](https://pre-commit.com/)

    pip install --user --upgrade pre-commit

Let Poetry install the rest from `pyproject.toml`

    poetry install

### Testing

[Coverage.py](https://coverage.readthedocs.io/en/7.2.2/) is used for test coverage, alongside [pytest](https://docs.pytest.org/en/7.2.x/), via the [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) plugin.

To run the tests directly, in you virtual environment, run `pytest --cov`.

To let nox run across multiple isolated environments, run `nox`.

To avoid nox recreating the virtual environments from scratch on each invocation, run `nox -r`.

Run a specific test with `nox -s tests -- tests/test_TESTNAME`.

### Static analysis

Autoformatting is performed with [Black](https://github.com/psf/black).

Run formatting with `nox -s black` or specify files/directors with `nox -s black -- file1 dir1 ...`.

Black auto-formatting is not run by default when running `nox` in isolation, it must be specified.

[Flake8](https://flake8.pycqa.org/en/latest/) is used for linting. Under the hood, it uses:

- [pylint](https://www.pylint.org/)
- [pyflakes](https://github.com/PyCQA/pyflakes) - invalid python code
  - errors reported as `F`
- [pycodestyle](https://github.com/pycqa/pycodestyle) - [PEP 8](https://peps.python.org/pep-0008/) style checking
  - `W` for warnings, `E` for errors
- [mccabe](https://github.com/PyCQA/mccabe) - code complexity
  - errors reported as `C`.
- [flake8-black](https://github.com/peterjc/flake8-black) plugin - adherence to Black code style
  - erros reported as `BLK`.
- [flake8-import-order](https://github.com/PyCQA/flake8-import-order) plugin - import grouping and ordering checked against the [Google styleguide](https://google.github.io/styleguide/pyguide.html?showone=Imports_formatting#313-imports-formatting)
  - errors reported as `I`
- [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear) plugin - various miscellaneous bugs and design problems
  - likely bugs reported as `B`
  - opinionated bugs reported as `B9`
  - `B950` replaces `E501` for max line length checking (adds tolerance margin of 10%)
- [flake8-bandit](https://github.com/tylerwince/flake8-bandit) plugin - uses [Bandit](https://github.com/PyCQA/bandit) to find common security issues
  - issues reported as `S`
- [flake8-annotations](https://github.com/sco1/flake8-annotations) plugin - detects absence of type annotations for functions
  - issues reported as `ANN`

All of these are configured in the `.flake8` file.

Run linting with `nox -s lint` or specify files/directoriess with `nox -s lint -- file1 dir1 ...`.

Import ordering is not auto-formatted although may in the future by migrating to [flake8-isort](https://github.com/gforcada/flake8-isort).

[Safety](https://github.com/pyupio/safety) is uesd for checking project dependencies against known security violations. For example, [insecure-package](https://pypi.org/project/insecure-package/).

Run it with `nox -s safety`.

#### Pre-commit

If you would like to enable the pre-commit hooks, run `pre-commit install`.

The hooks will run on files changed by the commit in question. To trigger hooks automatically run `pre-commit run --all-files`.
