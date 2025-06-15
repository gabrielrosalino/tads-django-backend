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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
    return render(request, 'registration/login.html')

@login_required #para apernas usuarios autenticados acessem a home
def home(request):
    return render(request, "home.html")



# --------- Alunos ----------
def matricular_aluno(request):
    return render(request, 'alunos/matricular_aluno.html', {'active_menu': 'alunos'})

def pesquisar_aluno(request):
    return render(request, 'alunos/pesquisar_aluno.html', {'active_menu': 'alunos'})


# --------- Disciplina ----------
def cadastrar_disciplina(request):
    return render(request, 'disciplinas/cadastrar_disciplina.html', {'active_menu': 'disciplina'})

def pesquisar_disciplina(request):
    return render(request, 'disciplinas/pesquisar_disciplina.html', {'active_menu': 'disciplina'})


# --------- Período Letivo ----------
def cadastrar_periodo(request):
    return render(request, 'periodos_letivos/cadastrar_periodo.html', {'active_menu': 'periodo'})

def pesquisar_periodo(request):
    return render(request, 'periodos_letivos/pesquisar_periodo.html', {'active_menu': 'periodo'})


# --------- Turmas ----------
def cadastrar_turma(request):
    return render(request, 'turmas/cadastrar_turma.html', {'active_menu': 'turmas'})

def pesquisar_turma(request):
    return render(request, 'turmas/pesquisar_turma.html', {'active_menu': 'turmas'})


# --------- Voluntários ----------
def cadastrar_voluntario(request):
    return render(request, 'voluntarios/cadastrar_voluntario.html', {'active_menu': 'voluntarios'})

def pesquisar_voluntario(request):
    return render(request, 'voluntarios/pesquisar_voluntario.html', {'active_menu': 'voluntarios'})