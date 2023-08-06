# Duke Typem 2D

[![PyPI](https://img.shields.io/pypi/v/DukeTypem2D)](https://pypi.org/project/DukeTypem2D/)
![Supported python versions](https://img.shields.io/pypi/pyversions/DukeTypem2D)
[![Documentation](https://github.com/orgua/DukeTypem2D/actions/workflows/sphinx_to_pages.yml/badge.svg)](https://orgua.github.io/DukeTypem2D/)
[![Pytest](https://github.com/orgua/DukeTypem2D/actions/workflows/python-app.yml/badge.svg)](https://github.com/orgua/DukeTypem2D/actions/workflows/python-app.yml)
[![CodeStyle](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Improves readability, spelling and expression of your text documents. The main focus will be scientific documents.

**WARNING**: as of now this is a non-working skeleton / prototype.

[Future Documentation](https://orgua.github.io/DukeTypem2D/)

[Current Documentation WIP](https://github.com/orgua/DukeTypem2D/tree/dev/docs/content/)

### Planned features:

- read in your documents (tex, markdown, reStructuredText, word, pdf, ...)
- check spelling
- hint at common mistakes
- evaluate choice of words
- improve readability and overall quality
- analyze phrasing and expression

### How can it be used?

- python package
- continuous integration via pre-commit
- web-API
- maybe a Language Server Protocol (LSP)

## Inspiration

A modern take on the original [Typo Nuke Tool](https://entorb.net/TypoNukeTool/) ([git](https://github.com/entorb/typonuketool)).

## Naming

- `duketypem`             -> CLI
- `DukeTypem2D`           -> PyPI, python-package-import (TODO: check)
- `.DukeTypem2D.yaml`   -> config-file (YAML or TOML excepted)
- `[tool.DukeTypem2D]`  -> entry in `pyproject.toml`

## Near Future ToDo

- begin inner workings
- enable documentation when public (link in conf.py)
- run pytest with coverage (and create tests)
-

## Latest Changes

- project bootstrap based on ['23 ruleset](https://blog.pronus.io/en/posts/python/how-to-set-up-a-perfect-python-project/)
- add configs for tools in toml
- add github-actions for testing
- add action for pypi-publish (with secret api-token)
- add project-meta-badges
- add to pypi
- documentation skeleton
- allow pre-commit hooking
- add doc for additional resources

- config-loader (implement, document, unittest)
