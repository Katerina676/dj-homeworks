from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, RetrieveAPIView


from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer


class CreateViewSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class UpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class UpdateMeasurment(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class OneSensor(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


