from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Voluntario, Aluno, Turma, Curso, Disciplina, Periodo_Letivo

# Registre seus modelos aqui
admin.site.register(Voluntario)
admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(Curso)
admin.site.register(Periodo_Letivo)


# Usuário Voluntarios
# Definir como os campos do modelo de cada 'Voluntario' será exibido e editado
class VoluntarioInline(admin.StackedInline): 
    model = Voluntario
    # O Django Admin não permitirá excluir objetos relacionados diretamente naquele inline. Ou seja, não existe um botão para excluir. Isso evita qualquer problema de excluir o inline do 'Voluntario' e manter um user "órfão" de informações extras adicionadas no modelo, como o número de telefone.
    can_delete = False 
    verbose_name_plural = 'Perfil do Voluntário'
    fk_name = 'user' # Especifica a chave estrangeira para o User
    # Listar os campos do Voluntario que aparecem no user
    # fields = ['foto', 'telefone_contato', 'data_nascimento_voluntario', 'descricao_atividades', 'cpf', 'email']

# Definir como todos os 'Voluntario' serão exibidos. Essa classe é necessária para que o Django entenda que os campos de inclusão do 'Voluntario' foram customizadas
class CustomUserAdmin(BaseUserAdmin):
    # Adiciona as informações da classe VoluntarioInline ao User
    inlines = (VoluntarioInline,)
    # Adicionar campos do Voluntario na list_display do User
    list_display = ('username', 'email', 'is_staff', 'get_telefone_voluntario')
    # Incluir filtro de pesquisa
    list_filter = ["username"]
    # Ordenar exibição da lista "geral"
    ordering = ["username"]
    # Incluir Caixa de pesquisa
    search_fields = ["username"]
    # Trazer barra de ação para baixo.
    actions_on_bottom = True
    actions_on_top = False

    # O campo telefone_contato não existe no modelo User, por conta disso é necessário "capturar" os dados do modelo.
    def get_telefone_voluntario(self, instance):
        # Acessa o perfil Voluntario através do related_name 'voluntario'
        # definido no OneToOneField do modelo Voluntario.
        try:
            if hasattr(instance, 'voluntario') and instance.voluntario:
                return instance.voluntario.telefone_contato
        except Voluntario.DoesNotExist: 
            return None
        return None
    get_telefone_voluntario.short_description = 'Telefone (Voluntário)'

# 3. Desregistre o UserAdmin padrão
admin.site.unregister(User)

# 4. Registre o seu CustomUserAdmin
admin.site.register(User, CustomUserAdmin)



# --- Customização para o Modelo Disciplina ---
class CustomDisciplinaAdmin(admin.ModelAdmin):
    # 1. Campos a serem exibidos na lista (colunas)
    list_display = ('nome', 'area_conhecimento', 'status', 'curriculo')

    # 2. Campos para pesquisa
    search_fields = ('nome', 'area_conhecimento', 'status')

    # 3. Mover a barra de ações para a parte inferior
    actions_on_bottom = True
    actions_on_top = False

    # 4. Filtro lateral
    list_filter = ('area_conhecimento', 'status')

    # 5. ORDENAÇÃO PADRÃO: Exibir ativos primeiro, depois inativos.
    ordering = ('-status', 'nome')

# 5. Registre o seu CustomDisciplinaAdmin
admin.site.register(Disciplina, CustomDisciplinaAdmin)