from django.shortcuts import render
from projects.models import Projects
from resume.models import Job, Education

# Create your views here.
def index(request):
    template = "home/home_index.html"
    allProjects = Projects.objects.all()
    allJobs = Job.objects.all().order_by('start')
    allEducation = Education.objects.all().order_by('start')

    context = {
        'projects' : allProjects,
        'jobs': allJobs,
        'educations': allEducation,
    }
    return render(request, template, context)