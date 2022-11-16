from django.shortcuts import render
from django.http import HttpResponse

from .models import Carpark, Campus
import requests
import json


# Create your views here.
def index(request):
    carpark_dict = {}
    campuses = Campus.objects.all()
    for campus in campuses:
        carparks = Carpark.objects.filter(campus_id=campus)
        carpark_dict[campus.name] = carparks
        for carpark in carpark_dict[campus.name]:
            response = requests.get(f'http://mbezbradica.pythonanywhere.com/carparks/{carpark}')
            response = response.json()
            if 'spaces_available' in response:
                carpark.available_spaces = f"{response['spaces_available']} spaces available"
            else:
                carpark.available_spaces = "real time info not available"
            carpark.save()

    context = {'carparkinfo': carpark_dict}


from .models import Campus, Carpark
import requests


# Create your views here.
def index(request):
    context = {}
    return render(request, "parkatdcu/index.html", context)


def carparks(request):
    context = {}
    webservice_base_url = "http://mbezbradica.pythonanywhere.com/carparks/"
    try:
        campus_name = request.GET['campus']

        campus = Campus.objects.get(name__iexact=campus_name)

        carparks = Carpark.objects.filter(campus_id=campus)
    except Campus.DoesNotExist:
        return HttpResponse('<h1> There is no such campus in DCU. Please copy one of the following campuses "Glasnevin", "All Hallows, "St. Pats" and navigate back into ParkAtDCU by pressing the back button on the top left of this page and paste the desired campus into the searchbar of ParkAtDCU </h1>')

    carpark_info = []
    labels = []
    data = []
    for carpark in carparks:

        webservice_url = webservice_base_url + carpark.name

        realtime_info = requests.get(webservice_url).json()

        if 'spaces_available' in realtime_info:
            spaces_available = realtime_info['spaces_available']
        else:
            spaces_available = 'not available'

        carpark_info.append({
            'name': carpark.name,
            'spaces': carpark.spaces,
            'disabled_spaces': carpark.disabled_spaces,
            'spaces_available': spaces_available
        }
        )
        labels.append(carpark.name)
        data.append(spaces_available)
    context['campus'] = campus_name
    context['carparks'] = carpark_info
    context['labels'] = labels  # labels and data for pie chart display
    context['data'] = data

    return render(request, "parkatdcu/carparks.html", context)


def busstop(request):
    context = {}
    return render(request, "parkatdcu/busstop.html", context)  # busstop page


def map(request):
    context = {}
    return render(request, "parkatdcu/map.html", context)  # map page
