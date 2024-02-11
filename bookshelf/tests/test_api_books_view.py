import pytest


@pytest.mark.django_db
def test___api_books_view__success(client, create_books):
    response = client.get('/api/books/')
    assert response.status_code == 200
    assert response.json()['books'] == [
        {
            'id': 1,
            'title': 'Book 1',
            'author_full_name': 'Author 1',
            'year_of_publishing': 2020,
            'copies_printed': 10,
            'short_description': 'Short description 1',
        },
        {
            'id': 2,
            'title': 'Book 2',
            'author_full_name': 'Author 2',
            'year_of_publishing': 2021,
            'copies_printed': 5,
            'short_description': 'Short description 2',
        },
        {
            'id': 3,
            'title': 'Book 3',
            'author_full_name': 'Author 3',
            'year_of_publishing': 2022,
            'copies_printed': 3,
            'short_description': 'Short description 3',
        }
    ]


@pytest.mark.django_db
def test____api_books_view__empty(client):
    response = client.get('/api/books/')
    assert response.status_code == 200
    assert response.json()['books'] == []
