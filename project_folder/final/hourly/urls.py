from django.urls import path

from . import views

app_name = "hourly"

urlpatterns = [
    path('', views.HourlyListView.as_view(template_name='hourly/hourly_list.html'), name="hourly_list"),
    path('<int:pk>', views.HourlyDetailView.as_view(), name="hourly_detail"),
    # path('song_search',  views.SearchSongsListView.as_view(template_name='songs/song_search.html'), name="song_search"),
]