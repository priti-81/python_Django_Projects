from django.contrib import admin
from .models import CustomUser,UserSelection

# Register your models here.
@admin.register(CustomUser)
class Userinfo(admin.ModelAdmin):
    list_display=['username','contactno','email']

@admin.register(UserSelection)
class AmenitiesInfo(admin.ModelAdmin):
    list_display=['name']

