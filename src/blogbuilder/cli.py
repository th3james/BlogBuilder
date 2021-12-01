import argparse
from pathlib import Path

from blogbuilder.blog_builder import BlogBuilder

parser = argparse.ArgumentParser()
parser.add_argument("input_dir", help="Directory path containing the blog data")
parser.add_argument("output_dir", help="Path to ouput rendered blog")
args = parser.parse_args()


def cli_main() -> None:
    BlogBuilder().build(
        Path(args.input_dir),
        Path(args.output_dir),
    )
