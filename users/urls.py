from django.urls import path
from . import views


urlpatterns = [
    path('', views.sign_in),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
]