from django.test import TestCase
from django.contrib.auth.models import User
from .models import Notification

class NotificationModelTest(TestCase):
    def test_notification_creation(self):
        user1 = User.objects.create_user(username='actor', password='pass')
        user2 = User.objects.create_user(username='recipient', password='pass')

        notification = Notification.objects.create(
            recipient=user2,
            actor=user1,
            verb='liked your post'
        )

        self.assertEqual(notification.recipient, user2)
        self.assertEqual(notification.actor, user1)
        self.assertEqual(notification.verb, 'liked your post')

