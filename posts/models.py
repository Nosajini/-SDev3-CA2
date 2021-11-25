import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.expressions import OrderBy
from django.urls import reverse

# Create your models here.

class Board(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField
    
    class Meta:
        ordering = ('name',)
    
    def get_absolute_url(self):
        return reverse('posts:posts_by_board', args=[self.id])
    
    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post/')
    body = models.TextField(max_length=1245)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default=uuid.uuid4)
    
    class Meta():
        ordering = ('date',)
    
    def get_absolute_url(self):
       return reverse('posts:post_detail', args=[self.board.id, self.id])
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name="comments",
        null=False
    )
    image = models.ImageField(blank=True, upload_to='post/comment/')
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )

    def has_image(self):
        return self.image
    
    def __str__(self):
        return self.comment

    class Meta():
        ordering = ('date',)

