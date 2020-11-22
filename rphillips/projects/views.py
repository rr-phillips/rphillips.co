from django.shortcuts import render

# Create your views here.
def index(request):
    template = "projects/projects_index.html"

    # context = {
    #    'projects' : allProjects,
    #}

    return render(request, template)
