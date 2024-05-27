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
        context = super().get_context_data(**kwargs)
        context['hourly_search_form'] = HourlySearchForm
        return context
