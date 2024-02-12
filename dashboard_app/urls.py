# dashboard_app/urls.py

from django.urls import path
from .views import DashboardDataList

urlpatterns = [
    path('api/data/', DashboardDataList.as_view(), name='dashboard_data_list'),
]
