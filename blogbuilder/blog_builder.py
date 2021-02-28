from pathlib import Path


class BlogBuilder:
    def build(self, data_dir: Path, templates_dir: Path, output_dir: Path) -> None:
        output_dir.mkdir()
