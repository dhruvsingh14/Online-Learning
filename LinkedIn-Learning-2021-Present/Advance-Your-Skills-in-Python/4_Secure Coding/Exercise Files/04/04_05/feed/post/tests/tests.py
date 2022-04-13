from rest_framework import status

from rest_framework.test import APIClient

import pytest

from ..models import Post, Profile
from .test_utils import author, non_author, PostFactory


@pytest.mark.django_db
def test_author_permissions(client, author):
    """should only allow authors to read posts"""
    PostFactory(author=author)
    client.force_login(author)
    permitted_response = client.get('/posts/')

    assert permitted_response.status_code == status.HTTP_200_OK
    assert len(permitted_response.json()) == 1


@pytest.mark.django_db
def test_author_no_permissions(client, non_author):
    """should not allow non-authors to read posts"""
    client.force_login(non_author)
    blocked_response = client.get('/posts/')
    assert blocked_response.status_code == status.HTTP_403_FORBIDDEN
    assert (
        blocked_response.json()['detail']
        == 'You do not have permission to perform this action.'
    )


@pytest.mark.django_db
def test_post_content(client, author):
    post = PostFactory(author=author, text='hey')
    client.force_login(author)
    response = client.get('/posts/')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0] == {
        'author': author.username,
        'text': 'hey',
        'created': post.created.strftime('%a, %d %b %Y'),
    }
