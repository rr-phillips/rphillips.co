from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    template = "blog/blog_index.html"

    allPosts = BlogPost.objects.all()
    context = {
        'posts': allPosts
    }

    return render(request, template, context)

def detail(request, pk):
    template = "blog/blog_post.html"

    post = BlogPost.objects.get(pk=pk)
    context = {
        'post': post
    }

    return render(request, template, context)