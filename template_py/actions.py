"""File Change Actions."""

import os
import pathlib
import shutil
import tempfile

import template_py.configuration as _configuration
import template_py.licence as _licence


def convert_file(
    configuration: _configuration.Configuration, path: pathlib.Path
) -> None:
    """Convert file according to the configuration."""
    with tempfile.NamedTemporaryFile("w", delete=False) as result:
        result.write(configuration.sub(path.read_text()))
        os.replace(result.name, path)


def convert_module(
    configuration: _configuration.Configuration, path: pathlib.Path
) -> None:
    """Convert modules according to the configuration."""
    result = path.parent / configuration.sub(path.name) / "__init__.py"
    result.parent.mkdir()
    result.touch()
    shutil.rmtree(path)


def convert_licence(
    configuration: _configuration.Configuration, path: pathlib.Path
) -> None:
    """Convert licence according to the configuration."""
    path.write_text(_licence.text(configuration.licence))
