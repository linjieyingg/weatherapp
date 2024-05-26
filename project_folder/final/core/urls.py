from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path('', views.HomePageView.as_view(template_name='core/home.html'), name="main"),
    path('search',  views.search_view, name="search"),
]