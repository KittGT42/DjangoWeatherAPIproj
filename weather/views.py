from django.shortcuts import render
import requests
from .forms import CityForm

from weather.models import City

API_key = '3b9a8366b264faed41fa7f19a6bea239'

def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        city_name = city.name
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}'
        res = requests.get(url).json()
        citi_info = {
            'city': city_name,
            'temperature': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
        }

        all_cities.append(citi_info)
    context = {
        'citi_info': all_cities,
        'form': form
    }
    print(citi_info)
    return render(request, 'weather/index.html', context=context)
