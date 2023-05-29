from django.db import models
from datetime import datetime

# Create your models here.
class signupinfo(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    username=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    mobileNo=models.BigIntegerField()


