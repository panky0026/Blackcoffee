from django.contrib import admin
from .models import DashboardData
# Register your models here.

@admin.register(DashboardData)
class DashboardDataAdmin(admin.ModelAdmin):
    list_display = []