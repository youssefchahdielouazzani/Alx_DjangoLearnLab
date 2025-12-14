from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostsCommentsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(author=self.user, title='Test Post', content='Content')

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author.username, 'testuser')

    def test_comment_creation(self):
        comment = Comment.objects.create(post=self.post, author=self.user, content='Nice post')
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.content, 'Nice post')

