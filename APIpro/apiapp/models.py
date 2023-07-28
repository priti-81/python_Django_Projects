from django.db import models

# Create your models here.
class Bookinfo(models.Model):
    Title=models.CharField(max_length=50)
    Author=models.CharField(max_length=30)
    Isbn=models.IntegerField()
    Publisher=models.CharField(max_length=40)