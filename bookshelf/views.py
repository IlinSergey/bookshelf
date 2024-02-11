from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
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


def api_books_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return JsonResponse(data={'books': list(books.values())}, safe=False)


def api_book_detail_view(request: HttpRequest, book_id: int) -> HttpResponse:
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404
    book_data = {
        'id': book.id,
        'title': book.title,
        'author_full_name': book.author_full_name,
        'year_of_publishing': book.year_of_publishing,
        'copies_printed': book.copies_printed,
        'short_description': book.short_description
    }
    return JsonResponse(data=book_data, safe=False)
