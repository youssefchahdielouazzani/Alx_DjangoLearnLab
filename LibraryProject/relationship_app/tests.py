from django.test import TestCase
from .models import Author, Book, Library, Librarian

class RelationshipAppTests(TestCase):

    def setUp(self):
        # Création des objets pour les tests
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter 1", author=self.author)
        self.book2 = Book.objects.create(title="Harry Potter 2", author=self.author)
        self.library = Library.objects.create(name="Central Library")
        self.library.books.add(self.book1, self.book2)
        self.librarian = Librarian.objects.create(name="John Doe", library=self.library)

    def test_author_books(self):
        self.assertEqual(self.author.books.count(), 2)

    def test_library_books(self):
        self.assertEqual(self.library.books.count(), 2)

    def test_librarian_library(self):
        self.assertEqual(self.librarian.library.name, "Central Library")

