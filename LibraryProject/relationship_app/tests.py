from django.test import TestCase
from .models import Author, Book, Library, Librarian

class RelationshipAppTests(TestCase):
    def setUp(self):
        a = Author.objects.create(name="George Orwell")
        b = Book.objects.create(title="1984", author=a)
        l = Library.objects.create(name="City Library")
        l.books.add(b)
        Librarian.objects.create(name="Sara", library=l)

    def test_books_by_author(self):
        from .query_samples import get_books_by_author
        books = get_books_by_author("George Orwell")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "1984")

    def test_books_in_library(self):
        from .query_samples import get_books_in_library
        books = get_books_in_library("City Library")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "1984")

    def test_librarian_by_library(self):
        from .query_samples import get_librarian_by_library
        librarians = get_librarian_by_library("City Library")
        self.assertEqual(len(librarians), 1)
        self.assertEqual(librarians[0].name, "Sar
