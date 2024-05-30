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
from io import BytesIO
import urllib, base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from .hourly_search_form import HourlySearchForm

# Create your views here.

class HourlyListView(ListView):
    model = Hourly
    context_object_name = 'hourlys'

    def get_queryset(self):
        hourly = Hourly.objects.all()
        print(hourly)
        return Hourly.objects.order_by('date')
    
    def get_context_data(self, **kwargs):
        # context = super(HourlyListView, self).get_context_data(**kwargs)
        # context['hourly_search_form'] = HourlySearchForm()
        context = super().get_context_data(**kwargs)
        hourlys = self.get_queryset()
        data = pd.DataFrame(list(hourlys.values()))
        
        fig, ax = plt.subplots(figsize=(8, 6))
        time = data['date']
        print(time)
        print(data['temp_f'])

        fig, ax = plt.subplots()
        plt.plot(time, data['temp_f'], label='Temperature (°F)')
        plt.plot(time, data['precip_in'], label='Precipitation (in)')
        plt.plot(time, data['humidity'], label='Humidity')
        plt.plot(time, data['wind_mph'], label='Wind (mph)')
        plt.title("Hourly Weather Trends")
        plt.tight_layout()
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.xticks(rotation=45)
        
        graphData = BytesIO()
        plt.savefig(graphData, format='png', bbox_inches='tight')
        graphData.seek(0)
        string = base64.b64encode(graphData.read())
        graph =  urllib.parse.quote(string)

        context['graph'] = graph
        
        return context       

    
class HourlyDetailView(DetailView):
    model = Hourly
    context_object_name = 'hourly_details'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hourly_search_form'] = HourlySearchForm
        return context
    

