from django.shortcuts import render

# Create your views here.
# dashboard_app/views.py

from rest_framework import generics
from .models import DashboardData
from .serializers import DashboardDataSerializer

class DashboardDataList(generics.ListAPIView):
    queryset = DashboardData.objects.all()
    serializer_class = DashboardDataSerializer
