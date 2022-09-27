from django.shortcuts import render
from django.http import HttpResponse
from .models import Campus,Carpark

# Create your views here.

def index(request):
    campus_data = Campus.objects.all()
    carparks_in_campus = Carpark.objects.all()
    for Carpark in campus_data:
        carparks = Carpark.objects.filter(campus_id = campus.campus_id)
        carparks_in_campus[campus.name] = carparks
    print(carparks_in_campus)


    context = {
        'carparks_in_campus': carparks_in_campus
    }
    # retrieve carpark information from the database
    # add it to the context dictionary

    return render(request,"parkatdcu/index.html",context)
