from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from books.models import Book


def library_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'bookshelf/library.html', context={'books': books})


def book_detail_view(request: HttpRequest, book_id: int) -> HttpResponse:
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404
    return render(request, 'bookshelf/book_detail.html', context={'book': book})
