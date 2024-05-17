from django.shortcuts import render
from .models import Job
# Create your views here.


def home(request):

    jobs = Job.objects.all()

    context = {
        'jobs': jobs,
    }

    return render(request, 'dunamis/index.html', context)


def AboutView(request):
    context = {

    }

    return render(request, 'dunamis/about.html', context)

def jobs(request):
    context = {

    }
    
    return render(request, 'dunamis/jobs.html', context)
