from django.test import TestCase
from django.contrib.auth.models import User
from .models import Notification

class NotificationTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass')
        self.user2 = User.objects.create_user(username='user2', password='pass')

    def test_create_notification(self):
        notification = Notification.objects.create(
            actor=self.user1, recipient=self.user2, verb='liked your post'
        )
        self.assertEqual(notification.recipient, self.user2)

