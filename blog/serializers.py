from rest_framework import serializers
from .models import Tags, Blog, Comments


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
