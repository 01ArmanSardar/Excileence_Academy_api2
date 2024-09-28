from rest_framework import serializers
from .models import tution

class TuitionSerializers(serializers.ModelSerializer):
    class Meta:
        model = tution
        fields = "__all__"