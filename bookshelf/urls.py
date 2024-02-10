from django.contrib import admin
from django.urls import path

from bookshelf.views import library_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', library_view),
]
