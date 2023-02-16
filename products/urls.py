from . import views
from django.urls import path


urlpatterns = [
     path('',views.index, name = 'home'),
     path('new/',views.new, name = 'new'),
     path('login/',views.loginuser, name = 'login'),
     path('logout/',views.logoutuser, name = 'logout'),
     path('register/',views.registeruser, name = 'register'),
]