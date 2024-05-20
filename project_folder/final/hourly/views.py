from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.urls import reverse_lazy
from .models import Hourly
from weather.models import Observation
from django.contrib import messages
from django.db.models import Q

# Create your views here.

class HourlyListView(ListView):
    model = Hourly
    context_object_name = 'hourlies'
    template_name = 'weather/hourly_list.html'
    
class HourlyDetailView(DetailView):
    model = Hourly
    context_object_name = 'hourly_details'
    template_name = 'weather/hourly_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['observations'] = Observation.objects.filter(hourly_id=self.get_object())
        return context