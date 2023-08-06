import pytest
from assertpy import assert_that
from mock import mock

from pullnix.cli import cli


@pytest.fixture
def repo_clone():
    with mock.patch("pullnix.repository.clone") as repo_clone:
        yield repo_clone


def test_cli(tmp_path, repo_clone):
    config_path = tmp_path / "config.yml"
    root_path = tmp_path / "root"

    assert_that(root_path.exists()).is_false()

    with open(config_path, "w") as file:
        file.write(f"""
        root: {root_path}
        repos:
          - name: foo
            url: bar
        """)

    cli(config_path)

    assert_that(root_path.exists()).is_true()
    repo_clone.assert_called_once_with("bar", root_path / "foo")
