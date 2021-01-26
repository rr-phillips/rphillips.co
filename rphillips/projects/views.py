from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    template = 'projects/projects_index.html'

    allProjects = Projects.objects.all()
    context = {
       'projects' : allProjects,
    }

    return render(request, template, context)

def detail(request, pk):
    template = 'projects/projects_detail.html'

    project = Projects.objects.get(pk=pk)
    context = {
        'project': project
    }

    return render(request, template, context)
