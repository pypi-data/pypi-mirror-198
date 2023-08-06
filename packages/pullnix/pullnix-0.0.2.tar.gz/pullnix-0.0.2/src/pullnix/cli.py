from pathlib import Path

from .config import load_config
from . import repository


def cli(config_path="/etc/pullnix.yml"):
    config = load_config(config_path)

    root = Path(config.root)

    if not root.exists():
        root.mkdir()

    for repo in config.repos:
        repo_path = root / repo.name
        if not repo_path.exists():
            repository.clone(repo, repo_path)
        else:
            repository.update(repo, repo_path)


