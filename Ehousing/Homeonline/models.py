from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    contactno = models.CharField(max_length=15,default=123456789)


class SalerInfo(models.Model):
    status= (
    ("SELL","SELL"),
    ("RENT","RENT"),
    )
    HouseOwnerName=models.CharField(max_length=30)
    Area=models.IntegerField()
    Contactno=models.BigIntegerField()
    BHK=models.IntegerField()
    Status=models.CharField(max_length=10,choices=status)
    Upload_Image=models.ImageField(upload_to="images")
    House_Description=models.TextField()
    House_address=models.TextField()
    House_price=models.CharField(max_length=50)
    

class Amenities(models.Model):
    Amenities_Choices = [
        ('BalconyOutdoor', 'BalconyOutdoor'), 
        ('Kitchen', 'Kitchen'),
        ('TVDeckTeniss', 'TVDeckTeniss'),
        ('Sunroof', 'Sunroof'),
        ('RoomConcret', 'RoomConcret'),
        ('Hall', 'Hall'),
        ('Storeroom', 'Storeroom'),
        ('Parking', 'Parking'),
        ('Tubewel', 'Tubewel'),
        ('Water', 'Water'),
        ('Gallery', 'Gallery'),
        ('Solar', 'Solar'),
        ('Furniture', 'Furniture'),
    ]
        
    Saler_InfoId = models.ForeignKey(SalerInfo, null=True, on_delete=models.CASCADE)
    Add_Amenities = models.CharField(max_length=255, choices=Amenities_Choices, blank=True, default=None)
    video_file = models.FileField(upload_to='videos', blank=True, default=None)
