from django.shortcuts import render

def dashboard (request):
    return render(request, 'dashboard.html')
def cadastrar_aluno (request):
    return render(request, 'cadastrar_aluno.html')