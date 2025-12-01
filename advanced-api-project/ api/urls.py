from django.urls import path
from .views import (
    BookListCreateView,
    BookRetrieveUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateView.as_view(), name='book-detail'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]


