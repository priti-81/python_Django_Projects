from django.contrib import admin
from .models import Bookinfo

# Register your models here.
@admin.register(Bookinfo)
class  BookAdmin(admin.ModelAdmin):
    list_display=('id','Title','Author','Isbn','Publisher')
    ordering=['id']