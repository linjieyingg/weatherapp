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
from datetime import datetime
from .hourly_search_form import HourlySearchForm
from core.form import SearchForm

# Create your views here.

class HourlyListView(ListView):
    model = Hourly
    context_object_name = 'hourlys'

    def get_queryset(self):
        now = datetime.now().strftime("%Y-%m-%d %H:00")
        hourly = Hourly.objects.filter(date__gte =now)
        print(hourly)
        return hourly.order_by('date')
    
    def get_context_data(self, **kwargs):
        # context = super(HourlyListView, self).get_context_data(**kwargs)
        # context['hourly_search_form'] = HourlySearchForm()
        context = super().get_context_data(**kwargs)
        hourlys = self.get_queryset()
        data = pd.DataFrame(list(hourlys.values()))
        
        fig, ax = plt.subplots(figsize=(8, 6))
        # time = data['date'].dt.hour
        # print(data['date'].dt.hour)

        fig, ax = plt.subplots()
        plt.plot(data['temp_f'], label='Temperature (°F)')
        plt.plot(data['precip_in'], label='Precipitation (in)')
        plt.plot(data['humidity'], label='Humidity')
        plt.plot(data['wind_mph'], label='Wind (mph)')
        plt.title("Hourly Weather Trends")
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=5)
        ax.set_xlabel("Time (in hours from now)")


        graphData = BytesIO()
        plt.savefig(graphData, format='png', bbox_inches='tight')
        graphData.seek(0)
        string = base64.b64encode(graphData.read())
        graph =  urllib.parse.quote(string)

        context['graph'] = graph
        context['search_form'] = SearchForm()
        
        return context       

    
class HourlyDetailView(DetailView):
    model = Hourly
    context_object_name = 'hourly_details'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hourly_search_form'] = HourlySearchForm
        context['search_form'] = SearchForm()
        return context
    

