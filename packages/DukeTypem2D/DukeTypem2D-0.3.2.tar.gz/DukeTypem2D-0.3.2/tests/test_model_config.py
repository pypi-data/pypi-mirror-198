# TODO: feed path(s) with non-valid data
import pytest
from pydantic import ValidationError

from duke_typem import Configuration


def test_model_config_cwd_project():
    config = Configuration()
    config.project_path = "."


def test_model_config_cwd_exclude():
    config = Configuration()
    config.exclude_paths = ["."]


def test_model_config_invalid_project():
    with pytest.raises(ValueError):
        config = Configuration()
        config.project_path = [".", "more"]  # expects str


def test_model_config_invalid_exclude():
    with pytest.raises(ValueError):
        config = Configuration()
        config.exclude_paths = "."  # expects List[str]


def test_model_config_invalid_str():
    with pytest.raises(ValidationError):
        config = Configuration()
        config.exclude_paths = 123.6
        print(config.exclude_paths)
        print(type(config.exclude_paths))
