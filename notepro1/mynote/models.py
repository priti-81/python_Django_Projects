from django.db import models

# Create your models here.
class  noteSignup(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    city=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return (f'{self.name},{self.email},{self.mobile},{self.city},{self.password}')

class myModel(models.Model):
    Title=models.CharField(max_length=100)
    Technology=models.CharField(max_length=20)
    Explaination=models.TextField(null=True, blank=True)
    Files=models.FileField(upload_to='media')
