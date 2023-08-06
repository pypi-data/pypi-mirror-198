import pytest
from mock import mock
from mock.mock import call

from pullnix.config import Repo
from pullnix.repository import clone, update


@pytest.fixture
def run():
    with mock.patch("subprocess.run") as run:
        yield run


def test_clone_with_existing_target(tmp_path, run):
    target_path = tmp_path / "target"
    target_path.mkdir()

    clone(Repo("foo", "bar"), target_path)

    run.assert_not_called()


def test_clone_without_existing_target(tmp_path, run):
    target_path = tmp_path / "foo"

    clone(Repo("bar", "baz"), target_path)

    run.assert_called_once_with(["git", "clone", "baz"], cwd=tmp_path, check=True)


def test_update(tmp_path, run):
    target_path = tmp_path / "foo"

    update(Repo("bar", "baz", "quux"), target_path)

    run.assert_has_calls([
        call(["git", "fetch"], cwd=target_path, check=True),
        call(["git", "diff", "quux...origin/quux"], cwd=target_path, check=True)
    ])
