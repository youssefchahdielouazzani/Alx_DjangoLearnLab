from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Author, Book, Library, Librarian


def books_by_author(request, author_id):
    """
    View: Affiche tous les livres écrits par un auteur spécifique
    """
    author = get_object_or_404(Author, id=author_id)
    books = author.books.all()
    book_list = ", ".join(book.title for book in books)
    return HttpResponse(f"📚 Livres de {author.name}: {book_list}")


def books_in_library(request, library_id):
    """
    View: Liste tous les livres disponibles dans une bibliothèque
    """
    library = get_object_or_404(Library, id=library_id)
    books = library.books.all()
    book_list = ", ".join(book.title for book in books)
    return HttpResponse(f"🏛️ Livres dans {library.name}: {book_list}")


def librarian_of_library(request, library_id):
    """
    View: Affiche le bibliothécaire d'une bibliothèque
    """
    library = get_object_or_404(Library, id=library_id)
    librarian = getattr(library, 'librarian', None)
    if librarian:
        return HttpResponse(f"👨‍💼 Bibliothécaire de {library.name}: {librarian.name}")
    else:
        return HttpResponse(f"❌ Aucun bibliothécaire assigné à {library.name}")
