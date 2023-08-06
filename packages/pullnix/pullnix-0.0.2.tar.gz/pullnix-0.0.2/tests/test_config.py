from assertpy import assert_that

import pullnix
from pullnix.config import Repo


def test_load(tmp_path):
    config_path = tmp_path / "config.yml"
    with open(config_path, "w") as file:
        file.write("""
        repos:
          - name: foo
            url: git@github.com:bar/baz.git
        """)
    result = pullnix.config.load_config(config_path)

    assert_that(result).is_not_none()
    assert_that(result.root).is_equal_to("/var/lib/pullnix")
    assert_that(result.repos).contains_only(Repo("foo", "git@github.com:bar/baz.git"))
