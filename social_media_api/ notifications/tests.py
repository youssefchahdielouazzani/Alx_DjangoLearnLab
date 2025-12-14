from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post, Like
from .models import Notification

class NotificationTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass')
        self.user2 = User.objects.create_user(username='user2', password='pass')
        self.post = Post.objects.create(author=self.user1, content='Test Post')
        self.like = Like.objects.create(post=self.post, user=self.user2)
        Notification.objects.create(
            recipient=self.user1,
            actor=self.user2,
            verb='liked your post',
            target=self.post
        )

    def test_notification_creation(self):
        notification = Notification.objects.get(recipient=self.user1)
        self.assertEqual(notification.actor, self.user2)
        self.assertEqual(notification.verb, 'liked your post')

