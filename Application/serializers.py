from rest_framework import serializers
from .models import application

class applicationSerializers(serializers.ModelSerializer):
    class Meta:
        model =application
        fields ="__all__"