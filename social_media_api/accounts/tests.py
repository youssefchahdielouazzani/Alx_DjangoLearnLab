from django.test import TestCase
from rest_framework.test import APIClient
from .models import CustomUser

class FollowTestCase(TestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(username='user1', password='pass')
        self.user2 = CustomUser.objects.create_user(username='user2', password='pass')
        self.client = APIClient()
        self.client.login(username='user1', password='pass')

    def test_follow_user(self):
        response = self.client.post(f'/accounts/follow/{self.user2.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user2, self.user1.following.all())

    def test_unfollow_user(self):
        self.user1.following.add(self.user2)
        response = self.client.post(f'/accounts/unfollow/{self.user2.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(self.user2, self.user1.following.all())

