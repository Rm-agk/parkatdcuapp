from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen
import json
import requests

from .models import Carpark,Campus

def index(request):
    campus_name = Campus.objects.all()
    carpark_name = Carpark.objects.all()
    no_parking = Campus.objects.filter(carpark=None)
    errors = []
    live_data = []

    for carpark in carpark_name:
        response = requests.get("http://mbezbradica.pythonanywhere.com/carparks/" + carpark.name)
        if response.ok:
            live_data.append(json.loads(response.text))
        else:
            errors.append(carpark)

    context = {"carpark_name": carpark_name,
               "campus_name": campus_name,
               "no_parking": no_parking,
               "live_data": live_data,
               "errors": errors
               }

    return render(request, "parkatdcu/index.html", context)
