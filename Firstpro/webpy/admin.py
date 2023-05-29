from django.contrib import admin
from .models import studinfo

# Register your models here.
class studdata(admin.ModelAdmin):
    list_display=['name','mobile','city']

admin.site.register(studinfo,studdata)
