from django.urls import path,include
from Homeonline import views

urlpatterns = [
   path('',views.index),
]