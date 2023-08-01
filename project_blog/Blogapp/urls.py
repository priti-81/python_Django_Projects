from django.urls import path,include
from . import views

urlpatterns = [
   path('getalldata/',views.getalldata),
   path('updatedata/<int:id>',views.updatedata),
   path('getid/<int:id>',views.getid),
   path('deleteid/<int:id>',views.deleteid),
   path('postdata/',views.insertdata),
]
