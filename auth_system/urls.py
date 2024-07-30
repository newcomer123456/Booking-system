from django.urls import path
from auth_system import views
from django.contrib import admin
from .views import custom_admin_dashboard

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('admin/', admin.site.urls)
]