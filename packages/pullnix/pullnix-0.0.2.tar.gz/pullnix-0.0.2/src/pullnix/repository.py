import subprocess
from pathlib import Path

from .config import Repo


def clone(repo: Repo, repo_path: Path):
    if repo_path.exists():
        return
    name = repo_path.name
    subprocess.run(["git", "clone", repo.url], cwd=repo_path.parent, check=True)


def update(repo: Repo, repo_path: Path):
    subprocess.run(["git", "fetch"], cwd=repo_path, check=True)
    subprocess.run(["git", "diff", f"{repo.branch}...origin/{repo.branch}"], cwd=repo_path, check=True)
    return None
