from django.db import models



# Create your models here.
class BlogInfo(models.Model):
    Title=models.CharField(max_length=30,default='data')
    Content=models.CharField(max_length=70,default='data')
    Created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    Updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        ordering=('-Updated_at',)
    
   