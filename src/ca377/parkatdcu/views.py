from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    context = {}

    # retrieve carpark information from the database
    # add it to the context dictionary

    return render(request,"parkatdcu/index.html",context)
