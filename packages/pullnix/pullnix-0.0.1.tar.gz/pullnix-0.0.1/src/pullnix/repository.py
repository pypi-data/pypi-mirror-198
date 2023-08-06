import subprocess
from pathlib import Path


def clone(url: str, repo_path: Path):
    if repo_path.exists():
        return
    name = repo_path.name
    subprocess.run(["git", "clone", url], cwd=repo_path.parent, check=True)
