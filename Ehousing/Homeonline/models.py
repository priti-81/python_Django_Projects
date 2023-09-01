from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    contactno = models.CharField(max_length=15,default=123456789)



class UserSelection(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class SalerInfo(models.Model):
    status= (
    ("SELL","SELL"),
    ("RENT","RENT"),
    )
    HouseOwnerName=models.CharField(max_length=30)
    Area=models.PositiveIntegerField()
    Contactno=models.BigIntegerField()
    BHK=models.PositiveIntegerField()
    Status=models.CharField(max_length=10,choices=status)
    Upload_Image=models.ImageField(upload_to="images")
    House_Description=models.TextField()
    House_address=models.TextField()
    House_price=models.CharField(max_length=50)
    video_file = models.FileField(upload_to='videos', blank=True, default=None)
    amenities = models.ManyToManyField(UserSelection)
    
    def __str__(self):
        return self.HouseOwnerName










