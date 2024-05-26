from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.urls import reverse_lazy
from .models import Hourly
from weather.models import Observation
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
import requests
from datetime import datetime

from .hourly_search_form import HourlySearchForm

# Create your views here.

class HourlyListView(ListView):
    model = Hourly
    context_object_name = 'hourlys'
    
    def get_context_data(self, **kwargs):
        context = super(HourlyListView, self).get_context_data(**kwargs)
        context['hourly_search_form'] = HourlySearchForm()
        return context
    
class HourlyDetailView(DetailView):
    model = Hourly
    context_object_name = 'hourly_details'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        settaggio = Hourly.objects.get(attivo = True)
        context['date'] = {'data':settaggio.data}
        context['hourly_search_form'] = HourlySearchForm
        context['observations'] = Observation.objects.filter(hourly_id=self.get_object())
        return context

# def hourly_search_view(request):
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['hourly_search_form'] = HourlySearchForm
#     #     return context
#     if request.method == "GET":
#         form = HourlySearchForm(request.GET)
#         if form.is_valid():
#             search_input = form.cleaned_data["Search"]
#             # print(type(search_input))
#             search_result = searchAPI(search_input)
#             # return render(request, "hourly/hourly_search_results.html", context={
#             #     "search_input": search_input,
#             #     "search_result": search_result
#             # })
#             return update(search_result)

# def searchAPI(search_input):
#     # url = "https://weatherapi-com.p.rapidapi.com/current.json"
#     url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
#     querystring = {"q": search_input}
#     headers = {
#         "x-rapidapi-key": "82ce6fe0f2msh1b1cfd285dbcc80p1b3260jsn6c515c923b86",
#         "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
#     }
#     response = requests.get(url, headers=headers, params=querystring)
#     r = requests.get(url, headers=headers, params=querystring).json()
#     # update(r)
#     return response.json()
    
# def update(r):
#     today = datetime.now().strftime("%Y-%m-%d %H:00")
#     location = r['location']['name']
#     country = r['location']['country']
    
#     for day in r['forecast']['forecastday']:
#         for hour in day['hour']:
#             date = hour['time']
#             hourly_info = {
#                 'date': hour['time'],
#                 'location': location,
#                 'country': country,
#                 'condition': hour['condition']['text'],
#                 'condition_img':hour['condition']['icon'],
#                 'temp_f': hour['temp_f'],
#                 'feels_like': hour['feelslike_f'],
#                 'humidity': hour['humidity'],
#                 'uv': hour['uv'],
#                 'wind_mph': hour['wind_mph'],
#                 'wind_dir': hour['wind_dir'],
#                 'pressure_in' : hour['pressure_in'],
#                 'precip_in': hour['precip_in'],
#             }
#             ho = Hourly(**hourly_info)
#             if Hourly.objects.filter(date=ho.date).exists():
#                 continue
#             else:
#                 Hourly.objects.update_or_create(**hourly_info)
#         observation_info = {
#             'date' : day['date'],
#             'location': location,
#             'country' : country,
#             'condition' : day['day']['condition']['text'],
#             'condition_img' : day['day']['condition']['icon'],
#             'humidity': day['day']['avghumidity'],
#             'max_f': day['day']['maxtemp_f'],
#             'min_f': day['day']['mintemp_f'],
#             'wind_mph': day['day']['maxwind_mph'],
#             'precip_in': day['day']['totalprecip_in'],
#             'uv': day['day']['uv'],
#             'sunrise': datetime.strptime(day['astro']['sunrise'],"%I:%M %p"),
#             'sunset': datetime.strptime(day['astro']['sunset'],"%I:%M %p"),
#             'moonrise': datetime.strptime(day['astro']['moonrise'],"%I:%M %p"),
#             'moonset': datetime.strptime(day['astro']['moonset'],"%I:%M %p"),
#             'moon_phase': day['astro']['moon_phase'] 
#         }
#         obs = Observation(**observation_info)
#         if Observation.objects.filter(date=obs.date).exists():
#             continue
#         else:
#             Observation.objects.update_or_create(**observation_info)
#     return redirect('..')