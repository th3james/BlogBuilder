from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from blogbuilder.post_file_loader import PostFileLoader
from blogbuilder.post_repository import PostRepository
from blogbuilder.tests.factories import build_post, build_valid_post_content


class PostRepositoryTest(TestCase):
    def test_load_from_directory_when_directory_has_post(self) -> None:
        """
        given a directory with a post in it
        it returns a PostRepository with the loaded post
        """
        with TemporaryDirectory() as td:
            input_dir = Path(td)

            post_file_path = input_dir / "fancy-post.md"
            post_file_path.write_text(build_valid_post_content())

            post_repository = PostRepository.load_from_directory(input_dir)

            assert post_repository.posts == [
                PostFileLoader(input_dir).load(post_file_path)
            ]

    def test_load_from_directory_ignores_non_post_files(self) -> None:
        """
        given a directory with non-post files
        it ignores them
        """
        with TemporaryDirectory() as td:
            input_dir = Path(td)

            post_file_path = input_dir / "some-random-file.hat"
            post_file_path.touch()

            post_repository = PostRepository.load_from_directory(input_dir)

            assert post_repository.posts == []

    def test_recent_posts_doesnt_return_old_posts(self) -> None:
        """
        given six posts
        it doesn't return the oldest
        """
        posts = [
            build_post(timestamp=datetime.fromisoformat(f"{year}-01-01"))
            for year in range(2010, 2016)
        ]
        post_repository = PostRepository(posts)

        result = post_repository.recent_posts()
        assert posts[0] not in result

    def test_recent_posts_returns_newest(self) -> None:
        """
        given six posts
        it returns the newest posts, newest first
        """
        posts = [
            build_post(timestamp=datetime.fromisoformat(f"{year}-01-01"))
            for year in range(2010, 2016)
        ]
        post_repository = PostRepository(posts)

        result = post_repository.recent_posts()
        result_years = [p.timestamp.year for p in result]
        assert list(range(2015, 2010, -1)) == result_years

    def test_archive_returns_archive(self) -> None:
        assert False
