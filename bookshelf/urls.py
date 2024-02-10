from django.contrib import admin
from django.urls import path

from bookshelf.views import book_detail_view, library_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', library_view),
    path('books/<int:book_id>/', book_detail_view),
]
