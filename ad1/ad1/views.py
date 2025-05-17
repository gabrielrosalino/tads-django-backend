from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def dashboard (request):
    return render(request, 'dashboard.html')

def cadastrar_aluno (request):
    return render(request, 'cadastrar_aluno.html')

def configNotifications(request):
    return render(request, 'configNotifications.html')
