from django.contrib import admin
from .models import BlogInfo

# Register your models here.

@admin.register(BlogInfo)
class blogadmin(admin.ModelAdmin):
    list_display=['id','Title','Created_at','Updated_at']
    ordering=['id']