from django.shortcuts import render
from django.http import HttpResponse

from .models import Carpark, Campus

# Create your views here.
def index(request):
    # this is all that is needed for Part 1
    #carparks = Carpark.objects.all()
    #context = {'carparks':carparks}


    # Part 2
    carpark_dict = {}
    # retrieve  information from the database
    campuses = Campus.objects.all()
    for campus in campuses:
        carparks = Carpark.objects.filter(campus_id=campus) # find all carparks for a campus
        carpark_dict[campus.name] = carparks

    # add information to the context dictionary
    context = {'carparkinfo':carpark_dict}
    
    return render(request,"parkatdcu/index.html",context)

