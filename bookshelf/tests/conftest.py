import pytest

from books.models import Book


@pytest.fixture
def create_books():
    books = [
        Book.objects.create(
            title='Book 1',
            author_full_name='Author 1',
            year_of_publishing=2020,
            copies_printed=10,
            short_description='Short description 1',
        ),
        Book.objects.create(
            title='Book 2',
            author_full_name='Author 2',
            year_of_publishing=2021,
            copies_printed=5,
            short_description='Short description 2',
        ),
        Book.objects.create(
            title='Book 3',
            author_full_name='Author 3',
            year_of_publishing=2022,
            copies_printed=3,
            short_description='Short description 3',
        )
    ]
    yield books
    Book.objects.all().delete()
