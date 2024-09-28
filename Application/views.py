from django.shortcuts import render
from rest_framework import viewsets
from .serializers import applicationSerializers
from .models import application
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

class application(viewsets.ModelViewSet):
    queryset=application.objects.all()
    serializer_class =applicationSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        teacher_id=self.request.query_params.get('teacher_id')
        tution_id=self.request.query_params.get('tution_id')
        if teacher_id:
            queryset = queryset.filter(teacher_id=teacher_id)
        if tution_id:
            queryset = queryset.filter(tution_id_=tution_id)
        return queryset
    
def deleteapplication(request,pk):
    try:
        data=application.objects.get(pk=pk)
        data.delete()
        return Response({"message":"application deleted"})
    except:
        return Response({"message":"application deleted"})

        
    
