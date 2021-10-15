from rest_framework import generics
from blog.models import Blog
from .serializers import BlogSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pass

class PostDetail(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pass
