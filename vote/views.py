"""
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import VoteForm
from .models import Vote


class VoteListView(ListView):
    model = Vote
    template_name = 'vote_list.html'

class VoteList(ListView):
    model = Vote

    def get(self, request):
        votes = Vote.objects.all()
        return render(request, "vote_list.html", {'votes':votes})

class VoteCreateView(LoginRequiredMixin, CreateView):
    model = Vote
    form_class = VoteForm
    template_name = 'vote_new.html'
    
    def get_success_url(self):
        post_id = self.kwargs.get("post_id")
        board_id = self.kwargs.get("board_id")
        return reverse_lazy('posts:post_detail', kwargs={'board_id':board_id, 'post_id':post_id})

#def checkVotes():


"""