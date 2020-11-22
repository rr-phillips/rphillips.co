from django.shortcuts import render

# Create your views here.
def index(request):
    template = "resume/resume_index.html"

    # get all the pieces for it
    # add the context to the return

    return render(request, template)
