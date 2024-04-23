from django.shortcuts import render
from .models import Post

from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView

# Create your views here.

class PostList(ListView):
    model=Post
    ordering=('-created_at')
    #queryset=Post.objects.filter(active=True)
class PostDetail(DetailView):
    model=Post

    
    
class PostCreate(CreateView):
    model=Post
    fields=['title','content','image']
    template_name='post\post_create.html'
    success_url='/posts'

class PostDelete(DeleteView):
    model=Post
    template_name='post\delete_post.html'
    success_url="/posts"


class PostUpdate(UpdateView):
    model=Post
    template_name= 'post/update_post.html'
    fields = ['title', 'content', 'image']  
    success_url = '/posts'