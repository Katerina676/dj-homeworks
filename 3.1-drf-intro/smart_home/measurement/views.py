from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer


class DemoView(APIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

