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
    BlogTagsList,
    ExternalLinksList,
    ExternalLink,
    ImageUrlsList,
    LikeBlogPost,
    ImageUrl,
    LikesList
)

router = DefaultRouter()
router.register('blog', Blogs)
router.register('externallink', ExternalLink)
router.register('comments', Comment)
router.register('imageurls', ImageUrl)
urlpatterns = [
    path('createtag/', CreateTag.as_view()),
    path('tags/', ListTags.as_view()),
    path('blogs/', ListBlogs.as_view()),
    path('', include(router.urls)),
    path('commentslist/', CommentsList.as_view()),
    path('blogtags/', BlogTagsList.as_view()),
    path('createblogtags/', CreateBlogTags.as_view()),
    path('externallinkslist/', ExternalLinksList.as_view()),
    path('imageurlslist/', ImageUrlsList.as_view()),
    path('like/<_id>', LikeBlogPost.as_view()),
    path('likes/', LikesList.as_view())
]
