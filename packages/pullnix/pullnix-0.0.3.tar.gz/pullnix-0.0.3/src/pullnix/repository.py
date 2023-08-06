import subprocess
from pathlib import Path
from typing import List

from .config import Repo


def clone(repo: Repo, repo_path: Path):
    if repo_path.exists():
        return
    name = repo_path.name
    subprocess.run(["git", "clone", repo.url], cwd=repo_path.parent, check=True)


def update(repo: Repo, repo_path: Path) -> List[str]:
    subprocess.run(["git", "fetch"], cwd=repo_path, check=True)
    diff_result = subprocess.run(["git", "diff", f"{repo.branch}...origin/{repo.branch}", "--name-only"], cwd=repo_path,
                                 check=True, capture_output=True)
    files = split(diff_result.stdout.decode())
    if files:
        subprocess.run(["git", "pull"], cwd=repo_path, check=True)
    return files


def split(output: str):
    return [stripped for line in (output.split("\n")) if (stripped := line.strip())]
