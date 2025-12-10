from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Book

class BookViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(title="Test Book", author="Author")

    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
