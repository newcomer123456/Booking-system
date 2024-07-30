from django.urls import path
from auth_system import views
from django.contrib import admin

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout')
    
]