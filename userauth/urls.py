from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('login',views.loginPage,name="loginpage"),
    path('register',views.registerPage,name="registerpage"),
    path('registerHandle',views.registerHandle,name="registerHandle"),
    path('loginHandle',views.loginHandle,name="loginHandle"),
    path('logout',views.logoutHandle,name="logoutHandle"),
]
