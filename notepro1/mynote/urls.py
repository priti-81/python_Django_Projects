from django.urls import path
from . import views

urlpatterns = [
   path('',views.index),
   path('aboutus/',views.aboutus),
   path('contactus/',views.contactus),
   path('notes/',views.notes,name='note'),
   path('profile/',views.profile),
   path('update/',views.update),
   path('delete/',views.delete),
   
]