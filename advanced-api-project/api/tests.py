from django.test import TestCase
from .models import Author, Book


class AuthorBookModelTest(TestCase):
    def test_create_author_and_book(self):
        # Créer un auteur
        author = Author.objects.create(name="Test Author")

        # Créer un livre
        book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=author
        )

        # Vérifications
        self.assertEqual(author.name, "Test Author")
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, author)
