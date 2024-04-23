from django.shortcuts import render
from .models import Post

from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView

# Create your views here.

class PostList(ListView):
    model=Post
    ordering=('-created_at')
    queryset=Post.objects.filter(active=True)
class PostDetail(DetailView):
    model=Post
    
    
class PostCreate(CreateView):
    model=Post

class PostDelete(DeleteView):
    model=Post


class PostUpdate(UpdateView):
    model=Post