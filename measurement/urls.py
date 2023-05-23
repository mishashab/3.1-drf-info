from django.urls import path
from .views import SensorDetailView, MeasurementsView


urlpatterns = [
    path('sensors/', SensorDetailView.as_view()),
    path('measurements/', MeasurementsView.as_view())
]
