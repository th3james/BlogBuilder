from blogbuilder.post import Post
from datetime import datetime


def build_post(
    slug: str = "post-slug",
    title: str = "post title",
    body: str = "# hello\ncontent",
    timestamp: "datetime" = datetime(2021, 2, 3),
) -> Post:
    return Post(slug, title, body, timestamp)


def build_valid_post_content(
    title: str = "nice title",
    timestamp: str = "2021-09-07T19:53:44+00:00",
    body: str = "Nice body",
) -> str:
    return f"""title: {title}
timestamp: {timestamp}
body:
{body}"""
