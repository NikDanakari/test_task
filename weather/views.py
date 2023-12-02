from django.shortcuts import render
import requests
from .models import City, WeatherInfo
from .forms import CityForm
from datetime import date
from .serializers import WeatherSerializer


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a15b6096b06fb0f2f8977f1c46c0492a'

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()
    cities = City.objects.all() #return all the cities in the database
    weather_data = []
    
    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'date' : date.today()
        }
        weather_data = []  
        weather_data.append(weather) #add the data for the current city into our list
    serializer = WeatherSerializer(weather)
    context = {'weather_data' : [serializer.data], 'form' : form}
    return render(request, 'weather/weather.html', context) #returns the weather.html template