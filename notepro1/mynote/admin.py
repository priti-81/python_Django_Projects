from django.contrib import admin
from .models import noteSignup
# Register your models here.

class  signup(admin.ModelAdmin):
    list_display=['name','email']

admin.site.register(noteSignup,signup)