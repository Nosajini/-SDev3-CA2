from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model
from django.db import models
from django.urls.base import reverse
from django.views.generic import ListView, DetailView

from shop.models import Product
from .models import Post, Board, Comment, Vote
from .forms import ImageForm, CommentForm, VoteForm, VoteUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


# Create your views here.

class PostList(ListView):
    model = Post

    def get(self, request, board_id=None):
        board = None
        posts = None
        if board_id != None:
            board = get_object_or_404(Board, id = board_id)
            posts = Post.objects.filter(board = board)
        else:
            posts = Post.objects.all()
        
        return render(request, "post_list.html", {'board':board, 'posts':posts})


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostListHome(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post

    def get(self, request, board_id, post_id):
        try:
            post = Post.objects.get(board_id = board_id, id = post_id)
        except Exception as e:
            raise e
        return render(request, "post_detail.html", {'post':post})
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['body']
    template_name = 'post_edit.html'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:post_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = ImageForm    
    template_name = 'post_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_new.html'
    
    def get_success_url(self):
        post_id = self.kwargs.get("post_id")
        board_id = self.kwargs.get("board_id")
        return reverse_lazy('posts:post_detail', kwargs={'board_id':board_id, 'post_id':post_id})

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get("post_id")
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class VoteCreateView(LoginRequiredMixin, CreateView):
    model = Vote
    form_class = VoteForm
    template_name = 'comment_new.html'
    
    def get_success_url(self):
        post_id = self.kwargs.get("post_id")
        board_id = self.kwargs.get("board_id")
        return reverse_lazy('posts:post_detail', kwargs={'board_id':board_id, 'post_id':post_id})
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get("post_id")
        return super().form_valid(form)

class VoteListView(ListView):
    model = Vote

    def get(self, request):
        votes = Vote.objects.all()
        return render(request, "vote_list.html", {'votes':votes})
    
    def addVote(self, id):
        object = Vote.objects.get(id)
        if get_user_model() not in object.users_votes:
            object.users_votes.append(get_user_model())
            object.votes+=1
            return(reverse_lazy('posts:vote_list'))
    

class VoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Vote
    form_class = VoteForm
    template_name = 'vote_update.html'
    success_url = reverse_lazy('posts:vote_list')

def VoteDetail(request, id):
    vote = Vote.objects.get(pk=id)
    if request.method == 'POST' and request.user.username not in vote.users_votes:
        vote.users_votes.append(request.user.username)
        vote.votes += 1
        if vote.votes >= 5:
            Product.objects.create(name = (vote.post.title+" "+str(vote.category)[:-1]), category = vote.category, description = vote.description, price = 20,
                                             image = vote.post.image, stock = 0, available = False)
            vote.delete()
            return redirect('posts:vote_list')
        vote.save()
        return redirect('posts:vote_list')

    return render(request, 'vote_update.html', {'vote':vote})
