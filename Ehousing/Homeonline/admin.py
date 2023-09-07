from django.contrib import admin
from .models import CustomUser,UserSelection,SalerInfo

# Register your models here.
@admin.register(CustomUser)
class Userinfo(admin.ModelAdmin):
    list_display=['username','contactno','email']

@admin.register(UserSelection)
class AmenitiesInfo(admin.ModelAdmin):
    list_display=['name']

@admin.register(SalerInfo)
class Salerdata(admin.ModelAdmin):
    list_display=['HouseOwnerName','Area','Contactno','BHK','Status','Upload_Image','House_Description','House_address','House_price','video_file']
