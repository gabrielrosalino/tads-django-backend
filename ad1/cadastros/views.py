from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def dashboard (request):
    return render(request, 'dashboard.html')

def add_student (request):
    return render(request, 'add_student.html')

def configNotifications(request):
    return render(request, 'configNotifications.html')

def login(request):
    return render(request, 'login.html')

@login_required #para apernas usuarios autenticados acessem a home
def home(request):
    return render(request, "home.html")