from rest_framework import serializers
from .models import Bookinfo

class Bookserial(serializers.ModelSerializer):
    class Meta:
        model=Bookinfo
        fields='__all__'
