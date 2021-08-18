from blogbuilder.post import Post


def build_post(
    slug: str = "post-slug", title: str = "post title", body: str = "# hello\ncontent"
) -> Post:
    return Post(slug, title, body)


def build_valid_post_content(title: str = "nice title", body: str = "Nice body") -> str:
    return f"""title: {title}
body:
{body}"""
