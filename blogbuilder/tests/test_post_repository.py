from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from blogbuilder.post_repository import PostRepository


class PostRepositoryTest(TestCase):
    def test_get_all_returns_a_post(self) -> None:
        """
        given a directory with a post in it
        it returns a post for that file
        """
        input_dir = Path("blogbuilder/tests/post_repo_test_data")

        try:
            input_dir.mkdir(parents=True)

            post_file_path = input_dir / "fancy-post.md"
            post_file_path.touch()

            post_repository = PostRepository(input_dir)
            result = post_repository.get_all()

            assert Path("fancy-post.html") in [p.path for p in result]
        finally:
            rmtree(input_dir)
