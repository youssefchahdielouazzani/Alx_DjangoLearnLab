from django.contrib import admin
from django.urls import path
from books.views import BookListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', BookListView.as_view()),
]

