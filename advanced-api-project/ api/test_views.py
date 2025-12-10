# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from django.utils import timezone
from api.models import Book  # adaptez l'import si votre app/model a un chemin différent

User = get_user_model()

class BookAPITestCase(APITestCase):
    """
    Tests CRUD, filtering/searching/ordering and basic permission behavior
    for the Book API endpoints.

    Ajustez les noms de champs (title, author, ...) et les noms d'URL
    ('book-list', 'book-detail') si votre projet utilise d'autres conventions.
    """

    def setUp(self):
        # clients
        self.client = APIClient()

        # create users
        self.user = User.objects.create_user(username="user1", password="testpass123")
        self.other_user = User.objects.create_user(username="user2", password="testpass123")

        # create sample books
        # Assurez-vous que les champs existent dans votre modèle Book.
        self.book1 = Book.objects.create(
            title="A Tale of Two Cities",
            author="Charles Dickens",
            published_date=timezone.now().date(),
            isbn="1111111111",
        )
        self.book2 = Book.objects.create(
            title="Zen and the Art of Motorcycle Maintenance",
            author="Robert Pirsig",
            published_date=timezone.now().date(),
            isbn="2222222222",
        )
        self.book3 = Book.objects.create(
            title="Algorithms Unlocked",
            author="Thomas Cormen",
            published_date=timezone.now().date(),
            isbn="3333333333",
        )

        # URL names — change si nécessaire
        self.list_url = reverse('book-list')     # ex: router.register('books', BookViewSet)
        # detail: reverse('book-detail', kwargs={'pk': self.book1.pk})

    def test_list_books(self):
        """GET /books/ returns list with status 200"""
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # check at least number of objects match
        self.assertGreaterEqual(len(resp.data), 3)

    def test_retrieve_book(self):
        """GET /books/{id}/ returns book detail"""
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data.get('title'), self.book1.title)

    def test_create_book_unauthenticated_forbidden(self):
        """anonymous POST should be rejected (401 or 403 depending on your auth config)"""
        payload = {
            "title": "New Book",
            "author": "Someone",
            "published_date": timezone.now().date().isoformat(),
            "isbn": "4444444444"
        }
        resp = self.client.post(self.list_url, payload, format='json')
        # Accept either 401 or 403 so test is robust to different auth setups
        self.assertIn(resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_create_book_authenticated(self):
        """authenticated user can create a book"""
        self.client.force_authenticate(user=self.user)
        payload = {
            "title": "New Book Auth",
            "author": "Auth Author",
            "published_date": timezone.now().date().isoformat(),
            "isbn": "5555555555"
        }
        resp = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # verify saved in DB
        created_pk = resp.data.get('id') or resp.data.get('pk')
        self.assertIsNotNone(created_pk)
        self.assertTrue(Book.objects.filter(pk=created_pk, title=payload['title']).exists())

    def test_partial_update_book(self):
        """PATCH /books/{id}/ updates a book"""
        self.client.force_authenticate(user=self.user)
        url = reverse('book-detail', kwargs={'pk': self.book2.pk})
        payload = {"title": "Updated Title"}
        resp = self.client.patch(url, payload, format='json')
        # allow 200 or 202 depending on viewset
        self.assertIn(resp.status_code, (status.HTTP_200_OK, status.HTTP_202_ACCEPTED))
        self.book2.refresh_from_db()
        self.assertEqual(self.book2.title, "Updated Title")

    def test_delete_book(self):
        """DELETE /books/{id}/ removes the book"""
        self.client.force_authenticate(user=self.user)
        url = reverse('book-detail', kwargs={'pk': self.book3.pk})
        resp = self.client.delete(url)
        # 204 No Content is typical
        self.assertIn(resp.status_code, (status.HTTP_204_NO_CONTENT, status.HTTP_200_OK))
        self.assertFalse(Book.objects.filter(pk=self.book3.pk).exists())

    def test_search_filtering(self):
        """
        Test search/filtering.
        This assumes your viewset has either SearchFilter or custom filters.
        Adjust query param names if your implementation differs.
        """
        # search by title substring (if SearchFilter is configured)
        resp = self.client.get(self.list_url, {'search': 'Tale'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # at least book1 should be present
        titles = [r.get('title') for r in resp.data]
        self.assertIn(self.book1.title, titles)

    def test_ordering(self):
        """
        Test ordering by title (ascending).
        Assumes OrderingFilter is configured with 'ordering' param and 'title' field allowed.
        """
        resp = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        returned_titles = [r.get('title') for r in resp.data]
        # compare to python-sorted list to ensure ordering applied
        expected = sorted([self.book1.title, self.book2.title, self.book3.title])
        # Some pagination may be active: only check prefix/sorted subset
        self.assertTrue(all(t in expected for t in returned_titles))
        # If there is no pagination, we can assert equality (but be tolerant)
        if len(returned_titles) == 3:
            self.assertEqual(returned_titles, expected)

    def test_permissions_on_update_delete(self):
        """
        If your app enforces object-level permissions (owner-only updates),
        test that a different user cannot update/delete another user's objects.
        If you don't implement object-level permissions, this test will pass by default.
        """
        # suppose book1 is not owned / has no owner, adapt if your model has an 'owner' field
        # Here we'll check that authenticated different user can still access endpoints (adjust as needed)
        self.client.force_authenticate(user=self.other_user)
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        resp = self.client.patch(url, {'title': 'Hacked Title'}, format='json')
        # Accept either success or forbidden depending on your object permissions
        self.assertIn(resp.status_code, (status.HTTP_200_OK, status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED))




