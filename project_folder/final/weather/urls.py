from django.urls import path

from . import views
from hourly.views import HourlyListView

app_name = "weather"

urlpatterns = [
    path('', views.ObservationListView.as_view(template_name='weather/weather_list.html'), name="weather_list"),
    path('<int:pk>', views.ObservationDetailView.as_view(), name="weather_detail"),
    path("bis/<int:pk>", views.ObservationDetailbisView.as_view(), name="weather_detail_bis"),
    path("js/<int:pk>", views.ObservationDetailJsView.as_view(), name="weather_detail_js"),
    path("update_bis/<int:pk>", views.ObservationUpdatebisView.as_view(), name="weather_update_bis"),
    path("update/<int:pk>", views.ObservationUpdateView.as_view(), name="weather_update"),

]