from django.shortcuts import render

# Create your views here.
def index(request):
    template = "home/home_index.html"
    return render(request, template)