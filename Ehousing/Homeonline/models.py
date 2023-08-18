from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    contactno = models.CharField(max_length=15,default=123456789)



