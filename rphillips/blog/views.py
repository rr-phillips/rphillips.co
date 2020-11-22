from django.shortcuts import render

# Create your views here.
def index(request):
    template = "blog/blog_index.html"
    # get all the blog posts

    # context = {posts: allPosts}
    return render(request, template)