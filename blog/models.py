from django.core.validators import MinLengthValidator
from django.db import models
from authentication.models import User


class Blog(models.Model):
    """Blog Model"""
    title = models.CharField(max_length=256, null=False)
    body = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    """Comments model to add comments"""
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256, null=False, validators=[MinLengthValidator(1, "Comment should have "
                                                                                             "minimum length 1.")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ImageUrls(models.Model):
    """Image urls models"""
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    url = models.URLField(max_length=256, null=False)


class Tags(models.Model):
    """Tags model"""
    tag = models.CharField(max_length=256, validators=[MinLengthValidator(3,"Length of tag cannot be less than 3")], unique=True)

    def __str__(self):
        self.tag


class BlogTags(models.Model):
    """Attach tags to blogs"""
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

class ExternalLinks(models.Model):
    """Attach external links to blog"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    link = models.URLField(max_length=256, null=False)
    data = models.CharField(max_length=256, null=False)