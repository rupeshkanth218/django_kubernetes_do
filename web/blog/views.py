from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

class BlogList(ListView):
    model = Post
    template_name = "blogs.html"

class BlogDetail(DetailView):
    model = Post
    template_name = "blog.html"