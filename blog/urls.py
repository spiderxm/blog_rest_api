from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CreateTag,
    ListTags,
    ListBlogs,
    Blogs,
    Comment,
    CommentsList,
    CreateBlogTags,
    BlogTagsList
)

router = DefaultRouter()
router.register('blog', Blogs)
router.register('comments', Comment)
urlpatterns = [
    path('createtag/', CreateTag.as_view()),
    path('tags/', ListTags.as_view()),
    path('blogs/', ListBlogs.as_view()),
    path('', include(router.urls)),
    path('commentslist/', CommentsList.as_view()),
    path('blogtags/', BlogTagsList.as_view()),
    path('createblogtags/', CreateBlogTags.as_view())
]
