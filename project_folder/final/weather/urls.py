from django.urls import path

from . import views

app_name = "weather"

urlpatterns = [
    path('', views.ObservationListView.as_view(template_name='weather/weather_list.html'), name="weather_list"),
    path('<int:pk>', views.ObservationDetailView.as_view(), name="weather_detail"),
    # path('song_search',  views.SearchSongsListView.as_view(template_name='songs/song_search.html'), name="song_search"),
]