from django.urls import path
from . import views

urlpatterns = [
    path('', views.ram_data, name='ram'),  #the path for our ram view
]