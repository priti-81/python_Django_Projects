from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index ),
    path('login/',views.login),
    path('signup/',views.signup),
    path('mypage/',views.mypage,name='mypage'),
    path('userlogout/',views.userlogout),
    path('login/forgotpassword/',views.forgotpassword),
    path('password/',views.password),
   
]