from django.shortcuts import render, get_object_or_404 ,redirect
from .models import CarouselSlide
from .models import *
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

# def home(request):
#     return render(request,'index.html')

def home(request):
    services = Service.objects.all()
    carousel_slides = CarouselSlide.objects.all()
    return render(request, 'index.html', {'services': services,'carousel_slides': carousel_slides})

def contactus(request):
    return render(request, 'contactus.html')

def service(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})

def aboutus(request):
    services = Service.objects.all()
    return render(request, 'about_us.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    projects = Project.objects.filter(service=service)
    return render(request, 'servicedetail.html', {'service': service, 'projects': projects})

def appointment(request):
    if request.method == 'POST':
        Customer_name = request.POST.get('cname')
        Customer_email = request.POST.get('cmail')
        mobile_number = request.POST.get('cnumber')
        service_type = request.POST.get('service_type')
        message = request.POST.get('message')

        appointment = Appointment(
            Customer_name=Customer_name,
            Customer_email=Customer_email,
            mobile_number=mobile_number,
            service_type=service_type,
            message=message
        )
        appointment.save()
        return redirect (home)
    return render (request, 'index.html')





