import pytest


@pytest.mark.parametrize('id_, expected_status, expected_title', [
    (1, 200, b'Book 1'),
    (2, 200, b'Book 2'),
    (3, 200, b'Book 3'),
    ])
@pytest.mark.django_db
def test__book_detail_view__success(client, create_books, id_, expected_status, expected_title):
    response = client.get(f'/books/{id_}/')
    assert response.status_code == expected_status
    assert expected_title in response.content


@pytest.mark.django_db
def test__book_detail_view__not_found(client, create_books):
    response = client.get('/books/4/')
    assert response.status_code == 404
