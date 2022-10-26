from django.shortcuts import render
from .models import Carpark, Campus

def index(request):
    campus_list = Campus.objects.all()
    carpark_list = Carpark.objects.all()
    noparking = Campus.objects.filter(carpark=None)

    context = {'carpark_list': carpark_list,
               'campus_list': campus_list,
               'noparking': noparking
               }


    return render(request, "parkatdcu/index.html", context)
