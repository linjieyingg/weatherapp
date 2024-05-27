from django.urls import path

from . import views
from hourly.views import HourlyListView

app_name = "weather"

urlpatterns = [
    path('', views.ObservationListView.as_view(template_name='weather/weather_list.html'), name="weather_list"),
    path('<int:pk>', views.ObservationDetailView.as_view(), name="weather_detail"),
    # path('<int:weather_id>/hourly/', HourlyListView.as_view(), name='hourly_list'),
    # path('song_search',  views.SearchSongsListView.as_view(template_name='songs/song_search.html'), name="song_search"),
]