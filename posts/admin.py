from django.contrib import admin
from django.db.models.base import Model
from .models import Post, Comment, Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ['name']


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ("board", "title", "author", "date", "id")
    inlines = [
        CommentInline
    ]
    list_per_page = 10

admin.site.register(Board)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
