from django.contrib import admin

from .models import Voluntario

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
