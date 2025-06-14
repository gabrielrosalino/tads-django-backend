from django.urls import path, include
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('configNotifications/', views.configNotifications, name='configNotifications'),
    path('add_student/', views.add_student, name = 'add_student'),
    path('login/', views.login, name = 'login'),
    path('home/', views.home, name="home"),
]