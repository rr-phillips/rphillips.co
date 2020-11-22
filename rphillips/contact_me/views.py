from django.shortcuts import render

# Create your views here
def index(request):
    template = "contact_me/contact_index.html"

    return render(request, template)
