from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from blogbuilder.post_repository import PostRepository


class PostRepositoryTest(TestCase):
    def test_TODO_load_from_directory(self) -> None:
        assert False

    def test_get_all_returns_a_post_with_path(self) -> None:
        """
        given a directory with a post in it
        it returns a post with the relative path
        """
        input_dir = Path("blogbuilder/tests/post_repo_test_data")

        try:
            input_dir.mkdir(parents=True)

            post_file_path = input_dir / "fancy-post.md"
            post_file_path.touch()

            post_repository = PostRepository(input_dir)
            result = post_repository.get_all()

            assert Path("fancy-post.md") in [p.path for p in result]
        finally:
            rmtree(input_dir)

    def test_get_all_returns_a_post_with_source_path(self) -> None:
        """
        given a directory with a post in it
        it returns a post with the source path
        """
        input_dir = Path("blogbuilder/tests/post_repo_test_data")

        try:
            input_dir.mkdir(parents=True)

            post_file_path = input_dir / "fancy-post.md"
            post_file_path.touch()

            post_repository = PostRepository(input_dir)
            result = post_repository.get_all()

            assert post_file_path in [p.source_path for p in result]
        finally:
            rmtree(input_dir)
