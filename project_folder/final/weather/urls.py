from django.urls import path

from . import views
from hourly.views import HourlyListView

app_name = "weather"

urlpatterns = [
    path('', views.ObservationListView.as_view(template_name='weather/weather_list.html'), name="weather_list"),
    path('<int:pk>', views.ObservationDetailView.as_view(), name="weather_detail"),
<<<<<<< HEAD
    # path('form', views.WeatherCreateView.as_view(), name="observation_form"),
    path("update/<int:pk>", views.UpdateView.as_view(),
    name="weather_update"),
    # path('<int:weather_id>/hourly/', HourlyListView.as_view(), name='hourly_list'),
    # path('song_search',  views.SearchSongsListView.as_view(template_name='songs/song_search.html'), name="song_search"),
=======
    path("bis/<int:pk>", views.ObservationDetailbisView.as_view(), name="weather_detail_bis"),
    path("js/<int:pk>", views.ObservationDetailJsView.as_view(), name="weather_detail_js"),
    path("update_bis/<int:pk>", views.ObservationUpdatebisView.as_view(), name="weather_update"),

>>>>>>> main
]