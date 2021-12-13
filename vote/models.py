import uuid
from django.db import models
from shop.models import Category, Product
from posts.models import Post
# Create your models here.
"""
class Vote(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    ),
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name="vote",
        null=False
    ),
    description = models.CharField(max_length=255, default="None")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ('date',)
        verbose_name_plural = 'votes'
"""