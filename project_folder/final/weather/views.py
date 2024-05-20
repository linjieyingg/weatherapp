from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# from django.urls import reverse_lazy
from django.contrib import messages
from .models import Observation
from django.db.models import Q

class ObservationListView(ListView):
    model = Observation
    context_object_name = 'observations'
    template_name = 'weather/observation_list.html'
    
class ObservationDetailView(DetailView):
    model = Observation
    context_object_name = 'observation_details'
    template_name = 'weather/observation_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        return context