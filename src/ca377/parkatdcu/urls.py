from django.urls import path

from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('carparks/',views.carparks,name='carparks'),
]
