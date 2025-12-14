from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Like
from notifications.views import create_notification

class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if created:
            create_notification(actor=request.user, recipient=post.author, verb='liked your post', target=post)
            return Response({'status': 'post liked'})
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        deleted, _ = Like.objects.filter(post=post, user=request.user).delete()
        if deleted:
            return Response({'status': 'post unliked'})
        return Response({'status': 'not liked yet'}, status=status.HTTP_400_BAD_REQUEST)

