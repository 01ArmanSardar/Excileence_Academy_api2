from django.shortcuts import render
from user.models import teacher
from Tution.models import tution
from Application.models import application

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class DashboardStatView(APIView):
    def get(self, request):
        total_teachers = teacher.objects.count()
        data = {
            'total_teachers': teacher.objects.count(),
            'total_applications': application.objects.count(),
            'live_tuition_jobs': tution.objects.filter(available=True).count(),
        }
        return Response(data, status=status.HTTP_200_OK)
