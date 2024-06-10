from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Observation
from hourly.models import Hourly
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.base import TemplateView
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .forms import ObservationForm
from io import BytesIO
import urllib, base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, date
import pytz 
from pytz import timezone
import json
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.form import SearchForm
from django.shortcuts import redirect

class ObservationListView(LoginRequiredMixin, ListView):
    model = Observation
    context_object_name = 'observations'
    template_name = 'weather/weather_list.html'
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"
    
    def get_queryset(self):
        now = datetime.now().strftime("%Y-%m-%d")
        obs = Observation.objects.filter(date__gte =now)
        return obs.order_by('date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        observations = self.get_queryset()
        data = pd.DataFrame(list(observations.values()))
        if data.empty:
            context['message'] = 'Please search a location first'
            return context
        fig, ax = plt.subplots(figsize=(8, 6))
        date = data['date']

        fig, ax = plt.subplots()
        plt.plot(date, data['max_f'], label='Maximum Temperature (°F)')
        plt.plot(date, data['min_f'], label='Minimum Temperature (°F)')
        plt.plot(date, data['precip_in'], label='Precipitation (in)')
        plt.plot(date, data['humidity'], label='Humidity')
        plt.plot(date, data['wind_mph'], label='Wind (mph)')
        ax.set_xticks(date)
        ax.set_xlabel("Date") 
        plt.title("Weather Trends in the Next 3 Days")
        plt.tight_layout()
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=5)
        
        graphData = BytesIO()
        plt.savefig(graphData, format='png', bbox_inches='tight')
        graphData.seek(0)
        string = base64.b64encode(graphData.read())
        graph =  urllib.parse.quote(string)

        context['graph'] = graph
        context['search_form'] = SearchForm()

        return context

class ObservationDetailView(DetailView):
    model = Observation
    context_object_name = 'object'
    template_name = 'weather/weather_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        return context

class ObservationDetailbisView(TemplateView):
    template_name = "weather/weather_detailbis.html"
    
    def get(self, request, *args, **kwargs):
        observation = get_object_or_404(Observation, pk=self.kwargs["pk"])
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weather_id'] = self.kwargs["pk"]
        context['search_form'] = SearchForm()
        return context
    
class ObservationDetailJsView(View):
    def get(self, request, *args, **kwargs):
        weather = get_object_or_404(Observation, pk=self.kwargs["pk"])
        weather_js = model_to_dict(weather)
        weather_js["hourlys"] = []
        for hourly in weather.hourlys.values():
            hourly['date'] = hourly['date'].astimezone(timezone('America/New_York'))
            weather_js["hourlys"].append(hourly)
        return JsonResponse({"weather": weather_js})

class ObservationUpdatebisView(View):
    def post(self, request, *args, **kwargs):
        weather = get_object_or_404(Observation, pk=self.kwargs["pk"])
        # Create a form instance with POST data
        form = ObservationForm(request.POST, instance=weather)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "errors": form.errors})
        
class WeatherUpdateView(UpdateView):
    model = Observation
    #fields = ['name']
    form_class = ObservationForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, 
            messages.SUCCESS, "updated"
            )
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        weather_dict = model_to_dict(self.object)
        note_dict={}
        strdate = weather_dict.get("date").strftime("%Y-%m-%d")
        note_dict = {"date": strdate , "note": weather_dict.get("note")}
        print(note_dict)
        context["weather_dico"] = note_dict
        context['search_form'] = SearchForm()
        return context

    # comment the following line to show the error about not having an
    # success_url
    def get_success_url(self):
        return reverse_lazy("weather:weather_detail", args=[self.object.id])       

