from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from hourly.models import Hourly
from weather.models import Observation
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from datetime import datetime, date
from .form import SearchForm
import pytz
import pandas as pd
import numpy as np
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

class HomePageView(LoginRequiredMixin,TemplateView):
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"
    template_name = "core/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm
        return context
    
class CoreLoginView(LoginView):
    template_name = "core/login.html"
    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return redirect('')

def search_view(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            search_input = form.cleaned_data["Search"]
            search_result = searchAPI(search_input)
            if search_result == "No matching location found.":
                messages.error(request, "No matching location found.")
                return redirect('/')
            return update(search_result)

def searchAPI(search_input):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": search_input, 'days': 3}
    headers = {
        "x-rapidapi-key": "82ce6fe0f2msh1b1cfd285dbcc80p1b3260jsn6c515c923b86",
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    r = requests.get(url, headers=headers, params=querystring).json()
    if 'error' in r:
        return r['error']['message']
    return response.json()
    
def update(r):
    location = r['location']['name']
    country = r['location']['country']
    est = pytz.timezone('US/Eastern')
    today = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:00"),"%Y-%m-%d %H:00").astimezone(est).strftime("%Y-%m-%d %H:00")
    for day in r['forecast']['forecastday']:
        moonrise = day['astro']['moonrise']
        moonset = day['astro']['moonset']
        print('obs',day['date'])
        if(moonrise == 'No moonrise'):
            moonrise = datetime.min
        else: 
            moonrise = datetime.strptime(day['astro']['moonrise'],"%I:%M %p")
        if(moonset == 'No moonset'):
            moonset= datetime.min
        else: 
            print(moonset)
            moonset = datetime.strptime(day['astro']['moonset'],"%I:%M %p")
        observation_info = {
            'date' : day['date'],'location': location,'country' : country,
            'condition' : day['day']['condition']['text'],
            'condition_img' : day['day']['condition']['icon'],
            'humidity': day['day']['avghumidity'],
            'max_f': day['day']['maxtemp_f'],'min_f': day['day']['mintemp_f'],
            'wind_mph': day['day']['maxwind_mph'],
            'precip_in': day['day']['totalprecip_in'],'uv': day['day']['uv'],
            'sunrise': datetime.strptime(day['astro']['sunrise'],"%I:%M %p"),
            'sunset': datetime.strptime(day['astro']['sunset'],"%I:%M %p"),
            'moonrise': moonrise,
            'moonset': moonset,
            'moon_phase': day['astro']['moon_phase'] 
        }
        Observation.objects.update_or_create(date=observation_info['date'], defaults=observation_info)
        for hour in day['hour']:
            hourly_info = {
                'date': datetime.strptime(str(hour['time']),'%Y-%m-%d %H:%M').astimezone(est),
                'location': location,'country': country,
                'condition': hour['condition']['text'],'condition_img':hour['condition']['icon'],
                'temp_f': hour['temp_f'],'feels_like': hour['feelslike_f'],
                'humidity': hour['humidity'],'uv': hour['uv'],
                'wind_mph': hour['wind_mph'],'wind_dir': hour['wind_dir'],
                'pressure_in' : hour['pressure_in'],'precip_in': hour['precip_in'],
            }
            if (hour['time'] > today or hour['time'] == today):
                hourly, created = Hourly.objects.update_or_create(date=hourly_info['date'],defaults=hourly_info)
                print(hourly.date)
                id = Observation.objects.get(date= datetime.strptime(hourly.date.strftime('%Y-%m-%d'), '%Y-%m-%d').astimezone(est))

                # id = Observation.objects.get(date= datetime.strptime(hourly.date.strftime('%Y-%m-%d'), '%Y-%m-%d').astimezone(est))
                id.hourlys.add(hourly)
                id.save()   
    return redirect('hourly/')