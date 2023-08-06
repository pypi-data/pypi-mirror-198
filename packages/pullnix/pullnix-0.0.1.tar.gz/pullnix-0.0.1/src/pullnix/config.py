from dataclasses import dataclass, field
from typing import List

import yaml
from dacite import from_dict


@dataclass(frozen=True)
class Repo:
    name: str
    url: str


@dataclass(frozen=True)
class Config:
    repos: List[Repo] = field(default_factory=list)
    root: str = "/var/lib/pullnix"


def load_config(config_path="/etc/pullnix.yml") -> Config:
    with open(config_path) as f:
        # use safe_load instead load
        return from_dict(data_class=Config, data=yaml.safe_load(f))
