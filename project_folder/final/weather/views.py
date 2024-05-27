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
import base64
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class ObservationListView(ListView):
    model = Observation
    context_object_name = 'observations'
    template_name = 'weather/observation_list.html'
    
    def get_queryset(self):
        return Observation.objects.order_by('date')
    
class ObservationDetailView(DetailView):
    model = Observation
    context_object_name = 'observation_details'
    template_name = 'weather/observation_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['hourlys'] = Hourly.objects.filter(observation_id=self.get_object())
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