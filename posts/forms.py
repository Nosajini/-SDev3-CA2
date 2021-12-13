from django import forms
from django.db import models
from django import forms
from django.db.models import fields
from .models import Post, Comment, Vote

class ImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['board', 'title', 'body', 'image',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['image', 'comment']
        editable_fields = ['image', 'comment']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['category', 'description',]