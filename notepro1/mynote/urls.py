from django.urls import path
from . import views

urlpatterns = [
   path('',views.index),
   path('aboutus/',views.aboutus),
   path('contactus/',views.contactus),
   path('notes/',views.notes),
   path('profile/',views.profile),
   
]