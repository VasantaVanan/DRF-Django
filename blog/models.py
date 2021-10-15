from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    Title = models.CharField(max_length=250)
    Blog = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    def __str__(self):
        return self.Title