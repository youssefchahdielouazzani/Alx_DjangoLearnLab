from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(title='Test Book', author='Author', publication_year=2025)
        self.assertEqual(book.title, 'Test Book')
