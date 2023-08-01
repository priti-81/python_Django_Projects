from rest_framework import serializers
from .models import BlogInfo

class Blogserial(serializers.ModelSerializer):
    class Meta:
        model=BlogInfo
        fields='__all__'