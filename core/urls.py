from django.urls import path
from .views import DashboardStatView
urlpatterns = [
    path('stats/', DashboardStatView.as_view(), name='dashboard-stats'),
]