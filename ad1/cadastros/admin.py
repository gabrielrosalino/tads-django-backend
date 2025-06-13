from django.contrib import admin

from .models import Voluntario, Student

# Register your models here.
class VoluntarioAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Dados pessoais:", {
                "fields": ["nome"]
            }
        ),
        (   # Fieldset criado para testar a separação dos dados no Admin.
            "Foto:", {
                "fields" : ["foto"] 
            }
        )
    ]
    # Definir o que vai aparecer na lista "geral" de voluntarios.
    list_display = ["foto", "nome"]
    # Inclusão de filtro de pesquisa.
    list_filter = ["nome"]
    # Ordenação de exibição da lista "geral".
    ordering = ["nome"]
    # Caixa de pesquisa.
    search_fields = ["nome"]
    # Trazer barra de ação para baixo.
    actions_on_bottom = True
    actions_on_top = False
admin.site.register(Voluntario, VoluntarioAdmin)

@admin.register(Student) #pra nao precisar vaser igual a ultima linha do voluntario
class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Dados pessoais", {
            "fields": [
                "nome", "email", "contato", "nascimento",
                "nacionalidade", "naturalidade", "estado_civil"
            ]
        }),
        ("Dados familiares", {
            "fields": [
                "nome_pai", "escolaridade_pai",
                "nome_mae", "escolaridade_mae"
            ]
        }),
        ("Sócio-econômicos", {
            "fields": ["renda_familiar"]
        }),
        ("Endereço", {
            "fields": [
                "rua", "numero", "complemento",
                "bairro", "cidade", "estado", "cep"
            ]
        }),
        ("Institucionais", {
            "classes": ["collapse"],  # opcional: faz essa seção ficar recolhível
            "fields": ["cursos_interesse", "periodos"]
        }),
    ]

    # Colunas exibidas na listagem
    list_display  = ["nome", "email", "contato", "estado_civil", "cidade"]
    # Filtros laterais
    list_filter   = ["estado_civil", "estado", "nacionalidade"]
    # Campos pesquisáveis
    search_fields = ["nome", "email", "contato", "cidade"]
    # Ordem padrão
    ordering      = ["nome"]
    # Ações no rodapé
    actions_on_bottom = True
