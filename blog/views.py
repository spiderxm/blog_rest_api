from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from authentication.permissions import UserPermissionsForBlog, UserPermissionsForComments
from .serializers import TagSerializer, BlogSerializer, CommentSerializer
from .models import Blog, ImageUrls, ExternalLinks, Comments, Tags, BlogTags


class CreateTag(generics.CreateAPIView):
    """
    Create Tags
    """
    serializer_class = TagSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ListTags(generics.ListAPIView):
    """
    List Tags
    """
    serializer_class = TagSerializer
    queryset = Tags.objects.all()


class ListBlogs(generics.ListAPIView):
    """
    List Blogs
    """
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class Blogs(ModelViewSet):
    """Manage Operations on Blogs"""
    serializer_class = BlogSerializer
    permission_classes = [UserPermissionsForBlog, IsAuthenticated]
    queryset = Blog.objects.all()
    authentication_classes = [TokenAuthentication, ]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CommentsList(generics.ListAPIView):
    """List all the comments """
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()


class Comment(ModelViewSet):
    """Manage Operations on Comments"""
    serializer_class = CommentSerializer
    permission_classes = [UserPermissionsForComments, IsAuthenticated]
    queryset = Comments.objects.all()
    authentication_classes = [TokenAuthentication, ]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
