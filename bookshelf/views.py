from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from books.models import Book


def library_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'bookshelf/library.html', context={'books': books})
