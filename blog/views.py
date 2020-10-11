from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework import status
from authentication.permissions import UserPermissionsForBlog, UserPermissionsForComments
from .serializers import TagSerializer, BlogSerializer, CommentSerializer, BlogTagsSerialzer, BlogTagsSerialzerForList, \
    CommentSerializerForList, ExternalLinkSerializer, ImageUrlSerializer, LikeSerializer
from .models import Blog, ImageUrls, ExternalLinks, Comments, Tags, BlogTags, LikeBlog


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
    serializer_class = CommentSerializerForList
    queryset = Comments.objects.all()


class Comment(ModelViewSet):
    """Manage Operations on Comments"""
    serializer_class = CommentSerializer
    permission_classes = [UserPermissionsForComments, IsAuthenticated]
    queryset = Comments.objects.all()
    authentication_classes = [TokenAuthentication, ]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class BlogTagsList(generics.ListAPIView):
    """List all the the tags for various blogs"""
    serializer_class = BlogTagsSerialzerForList
    queryset = BlogTags.objects.all()


class CreateBlogTags(generics.CreateAPIView):
    """Attach tags with blogs"""
    serializer_class = BlogTagsSerialzer
    permission_classes = [IsAuthenticated]
    queryset = BlogTags.objects.all()
    authentication_classes = [TokenAuthentication, ]


class ExternalLinksList(generics.ListAPIView):
    """List all the the external links"""
    serializer_class = ExternalLinkSerializer
    queryset = ExternalLinks.objects.all()


class ExternalLink(ModelViewSet):
    """Attach external links with blogs"""
    serializer_class = ExternalLinkSerializer
    permission_classes = [IsAuthenticated]
    queryset = ExternalLinks.objects.all()
    authentication_classes = [TokenAuthentication, ]


class ImageUrlsList(generics.ListAPIView):
    """List all the the Image urls"""
    serializer_class = ImageUrlSerializer
    queryset = ImageUrls.objects.all()


class ImageUrl(ModelViewSet):
    """Attach external links with blogs"""
    serializer_class = ImageUrlSerializer
    permission_classes = [IsAuthenticated]
    queryset = ImageUrls.objects.all()
    authentication_classes = [TokenAuthentication, ]


class LikeBlogPost(APIView):
    """Create and delete Likes"""
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

    def post(self, request, _id):
        like = LikeBlog.objects.all().filter(blog_id=_id, user_id=self.request.user.id)
        if len(like) == 0:
            like = LikeBlog.objects.create(blog_id=_id, user_id=self.request.user.id)
            like.save()
            return Response({"message": "Like Created Successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Like is Already Created"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, _id):
        like = LikeBlog.objects.all().filter(blog_id=_id, user_id=self.request.user.id)
        if len(like) != 0:
            like = like[0]
            like.delete()
            return Response({"message": "Like Deleted"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"error": "Like is Already Deleted"}, status=status.HTTP_400_BAD_REQUEST)

class LikesList(generics.ListAPIView):
    """List all the the Likes"""
    serializer_class = LikeSerializer
    queryset = LikeBlog.objects.all()
