from django.test import TestCase
from rest_framework.test import APIClient
from .models import Book

class BookTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(title="Test Book", author="Author")

    def test_book_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)


