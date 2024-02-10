from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from books.models import Book


def library_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'bookshelf/library.html', context={'books': books})


def book_detail_view(request: HttpRequest, book_id: int) -> HttpResponse:
    book = Book.objects.get(id=book_id)
    return render(request, 'bookshelf/book_detail.html', context={'book': book})
