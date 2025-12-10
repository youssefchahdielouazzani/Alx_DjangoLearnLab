from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book
from django.urls import reverse

class BookAPITestCase(TestCase):

    def setUp(self):
        # Test client
        self.client = APIClient()

        # Create a user
        self.user = User.objects.create_user(username="testuser", password="pass1234")

        # Create books
        self.book1 = Book.objects.create(
            title="Alpha",
            author="Author A",
            description="Desc A",
            published_year=2000
        )

        self.book2 = Book.objects.create(
            title="Beta",
            author="Author B",
            description="Desc B",
            published_year=2010
        )

        # URLs
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.id])

    # -----------------------------
    # LIST
    # -----------------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # -----------------------------
    # RETRIEVE
    # -----------------------------
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # -----------------------------
    # CREATE (AUTH REQUIRED)
    # -----------------------------
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="pass1234")

        payload = {
            "title": "New Book",
            "author": "Someone",
            "description": "Test",
            "published_year": 2024
        }

        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated_forbidden(self):
        payload = {
            "title": "New Book",
            "author": "Someone",
            "description": "Test",
            "published_year": 2024
        }

        response = self.client.post(self.list_url, payload, format="json")
        self.assertIn(response.status_code, [401, 403])

    # -----------------------------
    # UPDATE (AUTH REQUIRED)
    # -----------------------------
    def test_partial_update_book(self):
        self.client.login(username="testuser", password="pass1234")

        payload = {"title": "Updated Title"}

        response = self.client.patch(self.detail_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    # -----------------------------
    # DELETE
    # -----------------------------
    def test_delete_book(self):
        self.client.login(username="testuser", password="pass1234")

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # -----------------------------
    # SEARCH / FILTER / ORDER
    # -----------------------------
    def test_search_filtering(self):
        response = self.client.get(self.list_url, {"search": "Alpha"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering(self):
        response = self.client.get(self.list_url, {"ordering": "title"})
        titles = [item["title"] for item in response.data]
        self.assertEqual(titles, ["Alpha", "Beta"])




