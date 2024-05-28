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

    def get_context_data(self, **kwargs):
        context = super(HourlyListView, self).get_context_data(**kwargs)
        context['hourly_search_form'] = HourlySearchForm()
        
        hourlys = self.get_queryset()
        data = pd.DataFrame(list(hourlys.values()))
        
        fig, ax = plt.subplots(figsize=(8, 6))
        date = data['date']

        fig, ax = plt.subplots()
        plt.plot(date, data['temp_f'], label='Temperature (°F)')
        plt.plot(date, data['precip_in'], label='Precipitation (in)')
        plt.plot(date, data['humidity'], label='Humidity')
        plt.plot(date, data['wind_mph'], label='Wind (mph)')
        ax.set_xticks(date)
        ax.set_xlabel("Date", rotation=45) 
        plt.title("Weather Trends in the Next 24 Hours")
        plt.tight_layout()
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
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

