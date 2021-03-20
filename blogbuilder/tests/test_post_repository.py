from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from blogbuilder.post_repository import PostRepository
from blogbuilder.post_file_loader import PostFileLoader


class PostRepositoryTest(TestCase):
    def test_load_from_directory_when_directory_has_post(self) -> None:
        """
        given a directory with a post in it
        it returns a PostRepository with the loaded post
        """
        input_dir = Path("blogbuilder/tests/post_repo_test_data")

        try:
            input_dir.mkdir(parents=True)

            post_file_path = input_dir / "fancy-post.md"
            post_file_path.touch()

            post_repository = PostRepository.load_from_directory(input_dir)

            assert post_repository.posts == [
                PostFileLoader(input_dir).load(post_file_path)
            ]
        finally:
            rmtree(input_dir)
