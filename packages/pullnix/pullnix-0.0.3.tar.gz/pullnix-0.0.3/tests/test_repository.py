from subprocess import CompletedProcess

import pytest
from assertpy import assert_that
from mock import mock
from mock.mock import call

from pullnix.config import Repo
from pullnix.repository import clone, update, split


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

    run.side_effect = [None, CompletedProcess([], 0, "".encode(), "".encode())]

    result = update(Repo("bar", "baz", "quux"), target_path)

    assert_that(result).is_empty()
    assert_that(run.call_args_list).contains_only(
        call(["git", "fetch"], cwd=target_path, check=True),
        call(["git", "diff", "quux...origin/quux", "--name-only"], cwd=target_path, check=True, capture_output=True)
    )


def test_update_with_changes(tmp_path, run):
    target_path = tmp_path / "foo"

    run.side_effect = [None, CompletedProcess([], 0, "one\ntwo".encode(), "".encode()), None]

    result = update(Repo("bar", "baz", "quux"), target_path)

    assert_that(result).contains_only("one", "two")
    assert_that(run.call_args_list).contains_only(
        call(["git", "fetch"], cwd=target_path, check=True),
        call(["git", "diff", "quux...origin/quux", "--name-only"], cwd=target_path, check=True, capture_output=True),
        call(["git", "pull"], cwd=target_path, check=True),
    )


def test_lines():
    lines = split("")

    assert_that(lines).is_empty()


def test_lines_with_eol():
    lines = split("\n")

    assert_that(lines).is_empty()


def test_split_with_single_line():
    lines = split(" foo\n")

    assert_that(lines).contains_only("foo")


def test_split_with_multiple_lines():
    lines = split(" foo\n bar \n\n")

    assert_that(lines).contains_only("foo", "bar")
