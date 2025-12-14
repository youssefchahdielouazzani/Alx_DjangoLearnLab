from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        user = request.user
        posts = Post.objects.filter(author__in=user.following.all()).order_by('-created_at')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


