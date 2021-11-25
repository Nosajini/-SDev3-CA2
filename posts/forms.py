from django import forms
from django.db import models
from django import forms
from django.db.models import fields
from .models import Post, Comment

class ImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['board', 'title', 'body', 'image',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['image', 'comment']
        editable_fields = ['image', 'comment']
