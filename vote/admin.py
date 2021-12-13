from django.contrib import admin
from vote.models import Vote

# Register your models here.
class VoteAdmin(admin.ModelAdmin):
    list_display = ("post", "category", "votes")
    list_per_page = 5

admin.site.register(Vote, VoteAdmin)