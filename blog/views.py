from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import TagSerialiser
from .models import Blog, ImageUrls, ExternalLinks, Comments, Tags, BlogTags
class Blog(ModelViewSet):
    pass

class CreateTag(generics.CreateAPIView):
    serializer_class = TagSerialiser
    authentication_classes = [TokenAuthentication, IsAuthenticated]

class ListTags(generics.ListAPIView):
    serializer_class = TagSerialiser
    queryset = Tags.objects.all()


