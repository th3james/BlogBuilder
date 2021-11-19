from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from blogbuilder.post_file_loader import PostFileLoader
from blogbuilder.post_repository import Month, PostRepository
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

    def test_archive_when_empty(self) -> None:
        """
        given no posts
        returns empty archive
        """
        assert [] == list(PostRepository([]).archive())

    def test_archive_when_posts_are_in_different_months(self) -> None:
        """
        given posts in different months
        returns them in individual entries in different months
        """
        november_post = build_post(
            slug="november", timestamp=datetime.fromisoformat("2021-11-16")
        )
        december_post = build_post(
            slug="december", timestamp=datetime.fromisoformat("2021-12-09")
        )

        result = list(PostRepository([november_post, december_post]).archive())

        assert [
            Month.from_datetime(november_post.timestamp),
            Month.from_datetime(december_post.timestamp),
        ] == [r[0] for r in result]
        assert [["november"], ["december"]] == [[p.slug for p in r[1]] for r in result]

    def test_archive_when_posts_must_be_grouped_by_month(self) -> None:
        """
        given posts in the same month
        returns them in grouped under the same month
        """
        post_1 = build_post(
            slug="post 1", timestamp=datetime.fromisoformat("2021-11-16")
        )
        post_2 = build_post(
            slug="post 2", timestamp=datetime.fromisoformat("2021-11-19")
        )

        result = list(PostRepository([post_1, post_2]).archive())

        assert [Month.from_datetime(post_1.timestamp)] == [r[0] for r in result]
        assert [["post 1", "post 2"]] == [[p.slug for p in r[1]] for r in result]

    def test_archive_sorts_months(self) -> None:
        assert False

    def test_archive_sorts_posts(self) -> None:
        assert False
