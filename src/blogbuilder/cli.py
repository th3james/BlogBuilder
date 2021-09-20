import argparse
from pathlib import Path

from blogbuilder.blog_builder import BlogBuilder


parser = argparse.ArgumentParser()
parser.add_argument("blog_name", help="The name of the blog")
parser.add_argument("post_dir", help="Path to post directory")
parser.add_argument("templates_dir", help="Path to templates directory")
parser.add_argument("output_dir", help="Path to ouput rendered blog")
args = parser.parse_args()


def cli_main() -> None:
    BlogBuilder().build(
        args.blog_name,
        Path(args.post_dir),
        Path(args.templates_dir),
        Path(args.output_dir),
    )
