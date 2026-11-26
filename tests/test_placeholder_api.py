import pytest

from helpers import assert_valid_response, get

PLACEHOLDER_API = "https://jsonplaceholder.typicode.com"


def test_get_all_posts():
    response = get(f"{PLACEHOLDER_API}/posts")

    data = assert_valid_response(response, "posts.json")
    assert len(data) == 100


@pytest.mark.parametrize("post_id", [1, 2])
def test_post_comments(post_id):
    response = get(f"{PLACEHOLDER_API}/posts/{post_id}/comments")

    data = assert_valid_response(response, "comments.json")
    assert len(data) > 0
    assert all(comment["postId"] == post_id for comment in data)


@pytest.mark.parametrize("user_id", [1, 2])
def test_user_todos(user_id):
    response = get(f"{PLACEHOLDER_API}/users/{user_id}/todos")

    data = assert_valid_response(response, "todos.json")
    assert len(data) > 0
    assert all(todo["userId"] == user_id for todo in data)


@pytest.mark.parametrize("album_id", [1, 2])
def test_album_photos(album_id):
    response = get(f"{PLACEHOLDER_API}/albums/{album_id}/photos")

    data = assert_valid_response(response, "photos.json")
    assert len(data) > 0
    assert all(photo["albumId"] == album_id for photo in data)


@pytest.mark.parametrize("user_id", [1, 2])
def test_user_posts(user_id):
    response = get(f"{PLACEHOLDER_API}/users/{user_id}/posts")

    data = assert_valid_response(response, "posts.json")
    assert len(data) > 0
    assert all(post["userId"] == user_id for post in data)
