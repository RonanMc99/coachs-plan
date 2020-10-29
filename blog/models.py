from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from plans.models import Coach


class Post(models.Model):
    """ A list of plans that the user has access to """
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=150)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(Coach, null=True, blank=True, on_delete=models.SET_NULL)
