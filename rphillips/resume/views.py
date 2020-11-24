from django.shortcuts import render
from .models import Job, Education

# Create your views here.
def index(request):
    template = "resume/resume_index.html"

    # get all the pieces for it
    # add the context to the return

    allJobs = Job.objects.all().order_by('start')
    allEducation = Education.objects.all().order_by('start')
    context = {
        'jobs': allJobs,
        'educations': allEducation,
    }
    return render(request, template, context)
