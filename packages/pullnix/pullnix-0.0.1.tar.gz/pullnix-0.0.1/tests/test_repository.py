import pytest
from mock import mock

from pullnix.repository import clone

@pytest.fixture
def run():
    with mock.patch("subprocess.run") as run:
        yield run


def test_clone_with_existing_target(tmp_path, run):
    target_path = tmp_path / "target"
    target_path.mkdir()

    clone("foo", target_path)

    run.assert_not_called()

def test_clone_without_existing_target(tmp_path, run):
    target_path = tmp_path / "bar"

    clone("foo", target_path)

    run.assert_called_once_with(["git", "clone", "foo"], cwd=tmp_path, check=True)
