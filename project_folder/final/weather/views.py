from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Observation
from hourly.models import Hourly
from django.db.models import Q
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
from datetime import datetime
import pytz

class ObservationListView(ListView):
    model = Observation
    context_object_name = 'observations'
    template_name = 'weather/weather_list.html'
    
    def get_queryset(self):
        return Observation.objects.order_by('date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        observations = self.get_queryset()
        data = pd.DataFrame(list(observations.values()))
        
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
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
        graphData = BytesIO()
        plt.savefig(graphData, format='png', bbox_inches='tight')
        graphData.seek(0)
        string = base64.b64encode(graphData.read())
        graph =  urllib.parse.quote(string)

        context['graph'] = graph

        return context
    
class ObservationDetailView(DetailView):
    model = Observation
    context_object_name = 'object'
    template_name = 'weather/weather_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        return context

class ObservationDetailbisView(TemplateView):
    template_name = "weather/weather_detailbis.html"
    
    def get(self, request, *args, **kwargs):
        observation = get_object_or_404(Observation, pk=self.kwargs["pk"])
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weather_id'] = self.kwargs["pk"]
        return context
    
class ObservationDetailJsView(View):
    def get(self, request, *args, **kwargs):
        weather = get_object_or_404(Observation, pk=self.kwargs["pk"])
        weather_js = model_to_dict(weather)
        weather_js["hourlys"] = []
        for hourly in weather.hourlys.values():
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
        weather_dico = model_to_dict(self.object)
        context["weather_dict"] = weather_dico #works if replace {"key":test}
        return context

    # comment the following line to show the error about not having an
    # success_url
    def get_success_url(self):
        return reverse_lazy("weather:weather_detail", args=[self.object.id])       

def graphic(request):
    pos = np.arange(10)+ 2 
    
    df = pd.DataFrame(list(Observation.objects.all().values('date','min_f','max_f')))

    fig = plt.figure(figsize=(8, 3))
    ax = fig.add_subplot(111)

    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'graphic.html',{'graphic':graphic})

# def MyView(request, id): 
#     instance = get_object_or_404(Observation, id=id)
#     form = ObservationForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         form.save()
#         return redirect('')
#     return render(request, 'weather_update_bis.html', {'form': form}) 
