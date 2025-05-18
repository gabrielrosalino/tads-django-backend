from django.shortcuts import render

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
