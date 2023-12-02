from django.urls import path
from . import views

urlpatterns = [
    path('', views.RamInfoView.as_view(), name='ram'),  #the path for our ram view
]