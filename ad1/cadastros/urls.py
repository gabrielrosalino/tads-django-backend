from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('login/', views.login, name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', views.home, name="home"),
    # path('dashboard/', views.dashboard, name = 'dashboard'),
    # path('configNotifications/', views.configNotifications, name='configNotifications'),
    # path('add_student/', views.add_student, name = 'add_student'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # --------- Alunos ----------
    #path('alunos/matricular/', views.matricular_aluno, name='matricular_aluno'),
    path('alunos/pesquisar/', views.pesquisar_aluno, name='pesquisar_aluno'),
    path('alunos/matricular/', views.matricular_aluno, name = 'matricular_aluno'),

    # --------- Disciplina ----------
    path('disciplinas/cadastrar/', views.cadastrar_disciplina, name='cadastrar_disciplina'),
    path('disciplinas/pesquisar/', views.pesquisar_disciplina, name='pesquisar_disciplina'),

    # --------- Período Letivo ----------    
    path('periodos/cadastrar/', views.cadastrar_periodo, name='cadastrar_periodo'),
    path('periodos/pesquisar/', views.pesquisar_periodo, name='pesquisar_periodo'),

    # --------- Turmas ----------
    path('turmas/cadastrar/', views.cadastrar_turma, name='cadastrar_turma'),
    path('turmas/pesquisar/', views.pesquisar_turma, name='pesquisar_turma'),

    # --------- Voluntários ----------
    path('voluntarios/cadastrar/', views.cadastrar_voluntario, name='cadastrar_voluntario'),
    path('voluntarios/pesquisar/', views.pesquisar_voluntario, name='pesquisar_voluntario'),
]