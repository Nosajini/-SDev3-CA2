from django.db import models
from shop.models import Category, Product
from posts.models import Post
# Create your models here.

class Vote(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name="vote",
        null=False
    ),
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='Shirt')
    votes = models.IntegerField(default=0),
    date = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ('date',)
