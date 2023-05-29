from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('Resources/',views.Resources),
    path('Business/',views.Business),
    path('showdata/',views.showdata,name='showdata'),
    path('update/<int:id>',views.updatedata),
    path('delete/<int:id>',views.deletedata),
]