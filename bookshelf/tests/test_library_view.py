import pytest


@pytest.mark.django_db
def test_library_view__success(client, create_books):
    response = client.get('/books/')
    assert response.status_code == 200
    assert b'All Books' in response.content
    assert b'Book 1' in response.content
    assert b'Book 2' in response.content
    assert b'Book 3' in response.content
