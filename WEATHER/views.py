import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django import views
import requests
import json
import urllib.request
import datetime
from .forms import City_Form
import math
from django.template import RequestContext
from dotenv import load_dotenv
load_dotenv()
# Create your views here.


def weather(request):
    if request.method == 'POST':
        form = City_Form(request.POST)


    form = City_Form()
    city = request.GET.get('name')

    weather = os.getenv('openweathermap')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=ru&units=metric'.format(city, weather)
    response = requests.get(url.format(city))
    result = response.json()

    url_icon = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=ru&units=metric&mode=html'.format(city, weather)
    response_ic = requests.get(url_icon.format(city))
    response_icon = response_ic.url


    img = os.getenv('unsplash')

    url_img = 'https://api.unsplash.com/search/photos?query=downtown {}&client_id={}'.format(city, img)
    response_img = requests.get(url_img.format(city))
    res_img = response_img.json()
    img_city = res_img['results'][0]['urls']['small']


    coord_lan = result['coord']['lon']
    coord_lat = result['coord']['lat']
    weather_0 = result['weather'][0]['main']
    weather_1 = result['weather'][0]['description']
    temp = result['main']['temp']
    feels = result['main']['feels_like']
    min_t = result['main']['temp_min']
    max_t = result['main']['temp_max']
    pressure = result['main']['pressure']
    humidity = result['main']['humidity']
    visibility = result['visibility']
    wind_s = result['wind']['speed']
    wind_d = result['wind']['deg']
    if 348.75 < wind_d <= 11.25:
        wind_d = 'северный'
    elif 11.25 < wind_d <= 33.75:
        wind_d = 'северо северо-восточный'
    elif 33.75 < wind_d <= 56.25:
        wind_d = 'северо-восточный'
    elif 58.25 < wind_d <= 78.75:
        wind_d = 'восточный северо-восточный'
    elif 78.75 < wind_d <= 101.25:
        wind_d = 'восточный'
    elif 101.25 < wind_d <= 123.75:
        wind_d = 'восточный юго-восточный'
    elif 123.75 < wind_d <= 146.25:
        wind_d = 'юго-восточный'
    elif 146.25 < wind_d <= 168.75:
        wind_d = 'юго юго-восточный'
    elif 168.75 < wind_d <= 191.25:
        wind_d = 'южный'
    elif 191.25 < wind_d <= 213.75:
        wind_d = 'юго юго-западный'
    elif 213.75 < wind_d <= 236.25:
        wind_d = 'юго-западный'
    elif 236.25 < wind_d <= 258.75:
        wind_d = 'западный юго-западный'
    elif 258.75 < wind_d <= 281.25:
        wind_d = 'западный'
    elif 281.25 < wind_d <= 303.75:
        wind_d = 'западный северо-западный'
    elif 303.75 < wind_d <= 326.25:
        wind_d = 'северо-западный'
    elif 326.25 < wind_d <= 348.75:
        wind_d = 'северо северо-западный'
    sunrise_unix = result['sys']['sunrise']
    sunrise_uts = datetime.datetime.fromtimestamp(sunrise_unix)
    sunrise = sunrise_uts.strftime('%d-%m-%Y %H:%M:%S')
    sunset_unix = result['sys']['sunset']
    sunset_uts = datetime.datetime.fromtimestamp(sunset_unix)
    sunset = sunset_uts.strftime('%d-%m-%Y %H:%M:%S')
    icon = result['weather'][0]['icon']


    context = {'coord_lan': coord_lan,
               'coord_lat': coord_lat,
               'weather_0': weather_0,
               'weather_1': weather_1,
               'temp': temp,
               'feels': feels,
               'min_t': min_t,
               'max_t': max_t,
               'pressure': pressure,
               'humidity': humidity,
               'visibility': visibility,
               'wind_s': wind_s,
               'wind_d': wind_d,
               'sunrise': sunrise,
               'sunset': sunset,
               'icon': icon,
               'city': city,
               'form': form,
               'response_icon': response_icon,
               'img_city': img_city,
               }

    return render(request, 'weather.html', context=context)
