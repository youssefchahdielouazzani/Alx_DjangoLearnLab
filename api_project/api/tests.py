# api/tests.py
from django.test import TestCase
from .models import Book
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Book.objects.create(title="Book 1", author="Author A", published_date="2025-01-01")
        Book.objects.create(title="Book 2", author="Author B", published_date="2025-02-01")

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)



