from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name = 'index'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('configNotifications/', views.configNotifications, name='configNotifications'),
    path('add_student/', views.add_student, name = 'add_student'),
    path('login/', views.login, name = 'login'),
    path("home/", views.home, name="home"),
]
