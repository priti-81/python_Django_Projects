from django.urls import path,include
from Homeonline import views

urlpatterns = [
   path('',views.index),
   path('about/',views.about),
   path('bloggrid/',views.bloggrid),
   path('buy/',views.buy),
   path('rent/',views.rent),
   path('sell/',views.sell),
   path('update/',views.update),
   path('contact/',views.contact),
   path('signup/',views.signup,name='signup'),
   path('login/',views.login,name='login'),
]
