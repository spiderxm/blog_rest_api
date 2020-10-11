from rest_framework import serializers
from .models import Tags


class TagSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'tag']
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
