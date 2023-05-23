from rest_framework.generics import CreateAPIView, ListCreateAPIView, \
    RetrieveUpdateAPIView
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all().prefetch_related('measurements')
    serializer_class = SensorDetailSerializer


class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
