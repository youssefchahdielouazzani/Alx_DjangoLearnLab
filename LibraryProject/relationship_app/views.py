# LibraryProject/relationship_app/views.py
from django.shortcuts import render
from .models import Book

# Vue simple qui liste les livres et leurs auteurs
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

