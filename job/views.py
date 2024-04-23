from django.shortcuts import render
from .models import *
from labexam.settings import BASE_DIR
# Create your views here.

def index(request):
    # cars_data.objects.all().delete() #To Delete the data
    job = job_data.objects.all()
    return render(request, 'index.html', {'job':job, 'BASE_DIR':BASE_DIR})


def admin1(request):
    if request.method == 'POST':
        job = job_data()
        job.job_position = request.POST.get("job_position", False)
        job.job_company = request.POST.get("job_company", False)
        job.job_location = request.POST.get("job_location", False)
        job.job_salary = request.POST.get("job_salary", False)
        job.company_logo = request.FILES.get("company_logo", False)
        job.save()

    
    return render(request, 'upload.html')

def apply(request):
    if request.method == 'POST':
        apply = application_data()
        apply.name= request.POST.get("name", False)
        apply.email= request.POST.get("email", False)
        apply.phone= request.POST.get("phone", False)
        apply.resume = request.FILES.get("resume", False)
        apply.save()

    
    return render(request, 'apply.html')
