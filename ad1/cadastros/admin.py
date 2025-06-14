from django.contrib import admin

from .models import Voluntario, Student

# # Register your models here.
admin.site.register(Voluntario)
admin.site.register(Student)

# class VoluntarioAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (
#             "Dados pessoais:", {
#                 "fields": ["nome"]
#             }
#         ),
#         (   # Fieldset criado para testar a separação dos dados no Admin.
#             "Foto:", {
#                 "fields" : ["foto"] 
#             }
#         )
#     ]
#     # Definir o que vai aparecer na lista "geral" de voluntarios.
#     list_display = ["foto", "nome"]
#     # Inclusão de filtro de pesquisa.
#     list_filter = ["nome"]
#     # Ordenação de exibição da lista "geral".
#     ordering = ["nome"]
#     # Caixa de pesquisa.
#     search_fields = ["nome"]
#     # Trazer barra de ação para baixo.
#     actions_on_bottom = True
#     actions_on_top = False
# admin.site.register(Voluntario, VoluntarioAdmin)


# cadastros/admin.py
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# # Certifique-se que o nome do modelo importado aqui é EXATAMENTE como está em models.py
# # Se você chamou de Voluntario em models.py, aqui deve ser Voluntario.
# # Se chamou de PerfilVoluntario, aqui deve ser PerfilVoluntario.
# from .models import Voluntario # OU from .models import Voluntario (dependendo do nome que você usou)

# # Inline para o PerfilVoluntario
# class PerfilVoluntarioInline(admin.StackedInline):
#     # O 'model' aqui DEVE corresponder ao nome da classe do seu perfil em models.py
#     model = Voluntario # OU model = Voluntario
#     can_delete = False
#     verbose_name_plural = 'Perfil Adicional do Voluntário' # Ou o título que você quiser
#     # Liste AQUI os campos do SEU modelo de perfil que você quer que apareçam
#     fields = ['foto', 'telefone_contato', 'data_nascimento_voluntario', 'descricao_atividades']
#     # fk_name = 'user' # Geralmente não é necessário para OneToOneField com primary_key=True

# class CustomUserAdmin(BaseUserAdmin):
#     # AQUI é onde o inline é adicionado ao admin do User
#     inlines = (PerfilVoluntarioInline,) # Se o nome da classe inline for diferente, ajuste aqui

#     list_display = BaseUserAdmin.list_display + ('get_telefone_perfil',) # Exemplo

#     def get_telefone_perfil(self, instance):
#         # O nome do atributo aqui (perfil_voluntario) DEVE corresponder ao
#         # related_name definido no OneToOneField do seu modelo de perfil.
#         # Se related_name='perfil_voluntario', use 'perfil_voluntario'.
#         # Se related_name='voluntario', use 'voluntario'.
#         # Se não definiu related_name e a classe do perfil é PerfilVoluntario,
#         # o Django usa 'perfilvoluntario' (minúsculas).
#         if hasattr(instance, 'perfil_voluntario') and instance.perfil_voluntario:
#             return instance.perfil_voluntario.telefone_contato
#         return None
#     get_telefone_perfil.short_description = 'Telefone (Perfil)'

#     # Esta função pode não ser estritamente necessária nas versões mais recentes do Django
#     # para que o inline apareça na view de adicionar, mas não deve prejudicar.
#     # O 'extra = 1' no inline também ajuda.
#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             # Para mostrar o formulário inline ao adicionar um novo User,
#             # o Django geralmente faz isso automaticamente se 'extra' > 0 no inline.
#             # Se ainda não aparecer, você pode precisar instanciar o inline aqui.
#             # No entanto, o perfil só pode ser salvo DEPOIS que o User tem um ID.
#             # A criação via signals é uma forma de garantir isso.
#             # Para a exibição no form de ADICIONAR, o 'extra=1' (ou mais) no Inline é o mais comum.
#             # Se você definiu 'extra = 0' no inline, ele não aparecerá no 'add view'.
#             return super().get_inline_instances(request, obj) # Deixe o Django tentar primeiro
#         return super().get_inline_instances(request, obj)

# # DESREGISTRAR o UserAdmin padrão
# admin.site.unregister(User)
# # REGISTRAR o seu CustomUserAdmin
# admin.site.register(User, CustomUserAdmin)

# # NÃO ESQUEÇA DE REGISTRAR SEUS OUTROS MODELOS, COMO STUDENT
# from .models import Student # Supondo que Student está no mesmo models.py