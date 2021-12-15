import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import deletion
from django.db.models.expressions import OrderBy
from django.shortcuts import redirect
from django.urls import reverse

from shop.models import Category, Product

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

class Vote(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name="vote",
        null=False
    )
    description = models.CharField(max_length=255, default="None")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='postvote_category')
    votes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    users_votes = []    

    def incrementVote(self, user_username):
        print(self.post.title)
        print(self.users_votes)
        if user_username not in self.users_votes:
            self.users_votes.append(user_username)
            self.votes += 1

    def __str__(self):
        return self.post.title

    class Meta():
        ordering = ('date',)
        verbose_name_plural = 'votes'
        app_label = 'posts'
