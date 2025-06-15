from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .models import Aluno, Voluntario

from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponseForbidden


def role_required(allowed_roles):
    #Decorator que só permite acesso se request.user.voluntario.tipo_voluntario
    #estiver em allowed_roles. Caso contrário, 403.
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            # Incluir super usuário como habilitado pra acessar todas as partes do site.
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            if not request.user.is_authenticated:
                return redirect('login')
            # garante que exista perfil Voluntario
            if not hasattr(request.user, 'voluntario'):
                return HttpResponseForbidden()
            if request.user.voluntario.tipo_voluntario not in allowed_roles:
                return HttpResponseForbidden()
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator



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

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  
        else:
            return render(request, 'registration/login.html', {
                'error': 'Usuário ou senha inválidos'
            })
    
    return render(request, 'registration/login.html')

@login_required #para apernas usuarios autenticados acessem a home
def home(request):
    return render(request, "home.html")



# --------- Alunos ----------
@role_required(['COORDENADOR'])
@login_required
def matricular_aluno(request):
    return render(request, 'alunos/matricular_aluno.html', {'active_menu': 'alunos'})




@login_required
def pesquisar_aluno(request):
    # busca
    q = request.GET.get('q', '').strip()
    alunos = Aluno.objects.all()
    if q:
        alunos = alunos.filter(nome__icontains=q)

    # ordenação
    # campos permitidos para ordenar
    allowed = {'nome': 'nome', 'status': 'status'}
    order = request.GET.get('order', 'nome')
    direction = request.GET.get('dir', 'asc')
    if order not in allowed:
        order = 'nome'
    # prefixo '-' para desc
    prefix = '' if direction == 'asc' else '-'
    alunos = alunos.order_by(f"{prefix}{allowed[order]}")

    return render(request, 'alunos/pesquisar_aluno.html', {
        'alunos': alunos,
        'q': q,
        'order': order,
        'dir': direction,
        'active_menu': 'alunos',
    })




# --------- Disciplina ----------
@role_required(['COORDENADOR'])
@login_required
def cadastrar_disciplina(request):
    return render(request, 'disciplinas/cadastrar_disciplina.html', {'active_menu': 'disciplina'})

@login_required
def pesquisar_disciplina(request):
    return render(request, 'disciplinas/pesquisar_disciplina.html', {'active_menu': 'disciplina'})


# --------- Período Letivo ----------
@role_required(['COORDENADOR'])
@login_required
def cadastrar_periodo(request):
    return render(request, 'periodos_letivos/cadastrar_periodo.html', {'active_menu': 'periodo'})

@role_required(['COORDENADOR'])
@login_required
def pesquisar_periodo(request):
    return render(request, 'periodos_letivos/pesquisar_periodo.html', {'active_menu': 'periodo'})


# --------- Turmas ----------
@role_required(['COORDENADOR'])
@login_required
def cadastrar_turma(request):
    return render(request, 'turmas/cadastrar_turma.html', {'active_menu': 'turmas'})

@login_required
def pesquisar_turma(request):
    return render(request, 'turmas/pesquisar_turma.html', {'active_menu': 'turmas'})


# --------- Voluntários ----------
@role_required(['COORDENADOR'])
@login_required
def cadastrar_voluntario(request):
    return render(request, 'voluntarios/cadastrar_voluntario.html', {'active_menu': 'voluntarios'})

@role_required(['COORDENADOR'])
# @login_required
# def pesquisar_voluntario(request):
#     return render(request, 'voluntarios/pesquisar_voluntario.html', {'active_menu': 'voluntarios'})
@login_required 
def pesquisar_voluntario(request):
    q = request.GET.get('q', '').strip()
    order = request.GET.get('order', 'nome')
    direction = request.GET.get('dir', 'asc')

    voluntarios = Voluntario.objects.all()

    if q:
        voluntarios = voluntarios.filter(
            Q(nome__icontains=q) | Q(email__icontains=q)
        )

    allowed_sort_fields = {
        'nome': 'nome',
        'email': 'email',
        'tipo_voluntario': 'tipo_voluntario',
        'status': 'status_processo_voluntario' # Mapeia 'status' para o nome real do campo
    }
    sort_field = allowed_sort_fields.get(order, 'nome')

    if direction == 'desc':
        sort_field = f'-{sort_field}'

    voluntarios = voluntarios.order_by(sort_field)

    context = {
        'voluntarios': voluntarios,
        'q': q,
        'order': order,
        'dir': direction,
        'active_menu': 'voluntarios'
    }
    return render(request, 'voluntarios/pesquisar_voluntario.html', context)