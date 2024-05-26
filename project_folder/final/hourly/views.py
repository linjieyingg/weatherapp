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

import requests

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
        context['observations'] = Observation.objects.filter(hourly_id=self.get_object())
        return context

def hourly_search_view(request):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hourly_search_form'] = HourlySearchForm
        return context
    if request.method == "GET":
        form = HourlySearchForm(request.GET)
        if form.is_valid():
            search_input = form.cleaned_data["Search"]
            # print(type(search_input))
            search_result = searchAPI(search_input)
            return render(request, "hourly/hourly_search_results.html", context={
                "search_input": search_input,
                "search_result": search_result
            })

def searchAPI(search_input):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": search_input}
    headers = {
        "x-rapidapi-key": "de8f6f2a3fmsh850207b34ede80bp17e3d8jsnd9883430d914",
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    # print(response.json())
    return response.json()