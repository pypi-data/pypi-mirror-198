import pytest
from assertpy import assert_that
from mock import mock

from pullnix.cli import cli
from pullnix.config import Repo


@pytest.fixture
def repo_clone():
    with mock.patch("pullnix.repository.clone") as repo_clone:
        yield repo_clone


@pytest.fixture
def repo_update():
    with mock.patch("pullnix.repository.update") as repo_update:
        yield repo_update


def test_cli_clone(tmp_path, repo_clone):
    config_path = tmp_path / "config.yml"
    root_path = tmp_path / "root"

    with open(config_path, "w") as file:
        file.write(f"""
        root: {root_path}
        repos:
          - name: foo
            url: bar
        """)

    cli(config_path)

    assert_that(root_path.exists()).is_true()
    repo_clone.assert_called_once_with(Repo("foo", "bar"), root_path / "foo")


def test_cli_update(tmp_path, repo_update):
    config_path = tmp_path / "config.yml"
    root_path = tmp_path / "root"
    (root_path / "foo").mkdir(parents=True)

    with open(config_path, "w") as file:
        file.write(f"""
        root: {root_path}
        repos:
          - name: foo
            url: bar
        """)

    cli(config_path)

    repo_update.assert_called_once_with(Repo("foo", "bar"), root_path / "foo")
