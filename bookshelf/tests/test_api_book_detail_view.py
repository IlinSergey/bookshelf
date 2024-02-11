import pytest


@pytest.mark.parametrize('id_, status, title, author, year, copies, description', [
    (1, 200, 'Book 1', 'Author 1', 2020, 10, 'Short description 1'),
    (2, 200, 'Book 2', 'Author 2', 2021, 5, 'Short description 2'),
    (3, 200, 'Book 3', 'Author 3', 2022, 3, 'Short description 3'),
])
@pytest.mark.django_db
def test__api_book_detail_view__success(client, create_books, id_, status, title, author,
                                        year, copies, description):
    response = client.get(f'/api/books/{id_}/')
    assert response.status_code == status
    assert response.json() == {
        'id': id_,
        'title': title,
        'author_full_name': author,
        'year_of_publishing': year,
        'copies_printed': copies,
        'short_description': description,
    }


@pytest.mark.django_db
def test__api_book_detail_view__not_found(client, create_books):
    response = client.get('/api/books/4/')
    assert response.status_code == 404
