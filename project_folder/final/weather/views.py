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
    context_object_name = 'object'
    template_name = 'weather/weather_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['hourlys'] = Hourly.objects.filter(observation_id=self.get_object().id)
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
        
# class WeatherCreateView(CreateView):
#     model = Observation
#     form_class = ObservationForm

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.add_message(
#             self.request, messages.SUCCESS)
#             # ,
#             # 'Movie has been created'.format(
#             #     movie_name=self.object.name))
#         print('here', response)
#         return response
    
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # context["subject_list"] = Subject.objects.all()
#         print('contec', context)
#         return context
    
class UpdateView(UpdateView):
    model = Observation
    #fields = ['name']
    form_class = ObservationForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, 
            messages.SUCCESS, "updated"
            )
            # ,
            # 'Movie has been updated'.format(
            #     movie_name=self.object.name
            # ),
        
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # movie_dico = model_to_dict(self.object)
        # movie_dico["running_time"] = movie_dico["running_time"].strftime(
        #     "%H:%M:%S"
        # )
        # movie_dico["release_date"] = movie_dico["release_date"].strftime(
        #    "%Y-%m-%d"
        # )
        # actors = movie_dico["actors"]
        # movie_actor_list = []
        # for actor in actors:
        #     movie_actor_list.append({"id": actor.id, "name": actor.name})
        # movie_dico["actors"] = movie_actor_list
        # actor_list = list(Actor.objects.all().values())
        # context["movie_dict"] = movie_dico
        # context["actor_list"] = actor_list
        # print("context", context)
        return context

    # comment the following line to show the error about not having an
    # success_url
    # def get_success_url(self):
    #     return reverse_lazy("movies:movie_detail", args=[self.object.id])

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