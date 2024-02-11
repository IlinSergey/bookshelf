from django.contrib import admin
from django.urls import path

from bookshelf.views import (api_book_detail_view, api_books_view,
                             book_detail_view, library_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', library_view),
    path('books/<int:book_id>/', book_detail_view),
    path('api/books/', api_books_view),
    path('api/books/<int:book_id>/', api_book_detail_view),
]
