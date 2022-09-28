from django.shortcuts import render
from django.http import HttpResponse
from .models import Campus,Carpark

# Create your views here.

'''def index(request):
    campus_data = Campus.objects.all()
    carparks_in_campus = Carpark.objects.all()
    for Carpark in campus_data:
        carparks = Carpark.objects.filter(campus_id = campus.campus_id)
        carparks_in_campus[campus.name] = carparks
    print(carparks_in_campus)'''

def index(request):
    campus_name = Campus.objects.all()
    carpark_name = Carpark.objects.all()
    no_parking = Campus.objects.filter(carpark=None)
    context = {
        'campus_name': campus_name, 'carpark_name': carpark_name, 'no_parking': no_parking
    }
    # retrieve carpark information from the database
    # add it to the context dictionary

    return render(request,"parkatdcu/index.html",context)
