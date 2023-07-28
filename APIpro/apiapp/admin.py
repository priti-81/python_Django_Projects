from django.contrib import admin
from .models import Bookinfo

# Register your models here.
@admin.register(Bookinfo)
class  BookAdmin(admin.ModelAdmin):
    list_display=('Title','Author','Isbn','Publisher')