from rest_framework import serializers
from .models import Tags, Blog, Comments, BlogTags, ExternalLinks, ImageUrls, LikeBlog
from authentication.serializers import UserSerializer


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for Tag Model
    """

    class Meta:
        model = Tags
        fields = ['id', 'tag']
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }


class BlogTagsSerialzer(serializers.ModelSerializer):
    """
    Serializer for Blog Tags
    """

    class Meta:
        model = BlogTags
        fields = ['id', 'tag', 'blog']
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer fpr comments
    """

    class Meta:
        model = Comments
        fields = ['id', 'blog', 'user', 'comment', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'user': {
                'read_only': True
            },
            'created_at': {
                'read_only': True
            },
            'updated_at': {
                'read_only': True
            }

        }


class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for Blog Model
    """

    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'user', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'user': {
                'read_only': True
            },
            'created_at': {
                'read_only': True
            },
            'updated_at': {
                'read_only': True
            }

        }


class BlogTagsSerialzerForList(serializers.ModelSerializer):
    """
    Serializer for Blog Tags
    """
    tag = TagSerializer()
    blog = BlogSerializer()

    class Meta:
        model = BlogTags
        fields = ['id', 'tag', 'blog']
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }


class CommentSerializerForList(serializers.ModelSerializer):
    """
    Serializer fpr comments
    """
    user = UserSerializer()

    class Meta:
        model = Comments
        fields = ['id', 'blog', 'user', 'comment', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'user': {
                'read_only': True
            },
            'created_at': {
                'read_only': True
            },
            'updated_at': {
                'read_only': True
            }

        }


class ExternalLinkSerializer(serializers.ModelSerializer):
    """
    Serializer for external links for a blog
    """

    class Meta:
        model = ExternalLinks
        fields = ['id', 'blog', 'link', 'data']
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }


class ImageUrlSerializer(serializers.ModelSerializer):
    """
    Serializer for Image Urls of a Blog Post
    """
    class Meta:
        model = ImageUrls
        fields = ['id','blog', 'url']
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }

class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for Likes on a Blog Post
    """
    user = UserSerializer()
    class Meta:
        model = LikeBlog
        fields = ['id', 'blog', 'user']
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
