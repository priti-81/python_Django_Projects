from django.contrib import admin
from django.urls import path
from webpy import views

urlpatterns = [
    path('',views.index),
    path('business/',views.business),
    path('aboutus/',views.aboutus),
]
