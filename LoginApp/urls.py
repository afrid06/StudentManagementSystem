from django.urls import path

from LoginApp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login_fun,name='login'),
    path('register',views.register_fun,name='register'),
    path('readregister',views.read_register),
    path('readlogin',views.read_login),
    path('logout',views.logout_fun,name='logout')
]