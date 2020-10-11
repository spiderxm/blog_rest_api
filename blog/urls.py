from django.urls import path
from .views import (
    CreateTag,
    ListTags
)

urlpatterns = [
    path('createtag/', CreateTag.as_view()),
    path('tags/', ListTags.as_view())
]
