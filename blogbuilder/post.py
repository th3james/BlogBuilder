from dataclasses import dataclass
from pathlib import Path


@dataclass
class Post:
    path: Path
    source_path: Path
