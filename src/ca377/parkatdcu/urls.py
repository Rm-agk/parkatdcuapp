from django.urls import path

from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('carparks/',views.carparks,name='carparks'),
   path('busstop/',views.busstop,name='busstop'),
    path('map/',views.map,name='map'),
]
