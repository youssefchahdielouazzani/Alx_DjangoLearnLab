from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Créer un utilisateur admin et un utilisateur normal
        self.admin_user = User.objects.create_superuser(username='admin', password='admin123')
        self.regular_user = User.objects.create_user(username='user', password='user123')

        self.book = Book.objects.create(title="Test Book", author="Author A", price=10.0)
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])

    def test_get_books_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_as_admin(self):
        self.client.login(username='admin', password='admin123')
        data = {"title": "New Book", "author": "Author B", "price": 15.0}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_as_regular_user(self):
        self.client.login(username='user', password='user123')
        data = {"title": "New Book", "author": "Author B", "price": 15.0}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_as_admin(self):
        self.client.login(username='admin', password='admin123')
        data = {"title": "Updated Book"}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book_as_admin(self):
        self.client.login(username='admin', password='admin123')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
