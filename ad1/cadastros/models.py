from django.db import models
from django.contrib.auth.models import User


# # Modelo voluntário - Caso queiram criar um novo voluntário como "Cadastros", sem senha.
# class Voluntario(models.Model):
#     nome = models.CharField("Nome completo", max_length = 100)
#     foto = models.ImageField(upload_to='img/voluntarios', null=True, blank=True)
#     def __str__(self):
#         return self.nome

# Usuário voluntário
class Voluntario(models.Model): 
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='voluntario' 
    )
    foto = models.ImageField(
        "Foto Principal",
        upload_to='voluntarios/perfis/fotos/',
        null=True,
        blank=True
    )
    telefone_contato = models.CharField(
        "Telefone de Contato",
        max_length=20,
        blank=True
    )
    data_nascimento_voluntario = models.DateField(
        "Data de Nascimento",
        null=True,
        blank=True
    )
    descricao_atividades = models.TextField(
        "Descrição das Atividades/Interesses",
        blank=True
    )

    def __str__(self):
        return self.user.username 
    
# Modelo estudante.
class Aluno(models.Model):
    # Dados pessoais
    nome            = models.CharField("Nome completo", max_length=100)
    email           = models.EmailField("E-mail", unique=True)
    contato         = models.CharField("Contato", max_length=20, blank=True)
    nascimento      = models.DateField("Data de nascimento", null=True, blank=True)
    nacionalidade   = models.CharField("Nacionalidade", max_length=50, blank=True)
    naturalidade    = models.CharField("Naturalidade", max_length=50, blank=True)
    estado_civil    = models.CharField("Estado Civil", max_length=20, blank=True)

    # Dados familiares
    nome_pai        = models.CharField("Nome do Pai", max_length=100, blank=True)
    escolaridade_pai= models.CharField("Escolaridade do Pai", max_length=50, blank=True)
    nome_mae        = models.CharField("Nome da Mãe", max_length=100, blank=True)
    escolaridade_mae= models.CharField("Escolaridade da Mãe", max_length=50, blank=True)

    # Sócio-econômicos
    renda_familiar  = models.DecimalField("Renda familiar média", max_digits=10, decimal_places=2, null=True, blank=True)

    # Endereço
    rua             = models.CharField("Rua", max_length=200)
    numero          = models.CharField("Número", max_length=20)
    complemento     = models.CharField("Complemento", max_length=100, blank=True)
    bairro          = models.CharField("Bairro", max_length=100, blank=True)
    cidade          = models.CharField("Cidade", max_length=100, blank=True)
    estado          = models.CharField("Estado", max_length=2, blank=True)
    cep             = models.CharField("CEP", max_length=9, blank=True)

    # Institucionais
    cursos_interesse= models.JSONField("Cursos de Interesse", null=True, blank=True)
    periodos        = models.JSONField("Períodos", null=True, blank=True)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    STATUS = {
        0: "INATIVO",
        1: "ATIVO"
    }

    id_turma = models.AutoField(primary_key=True)
    nome = models.CharField("Nome da Turma", max_length=30, unique=True)
    capacidade = models.IntegerField("Capacidade de total de alunos na turma")
    data_inicio = models.DateField("Data de início da turma")
    data_fim = models.DateField("Data final da turma")
    status = models.IntegerField("0 - Inativo; 1 - Ativo", choices=STATUS)
    # TODO: id_periodo_letivo = models.ForeignKey(PeriodoLetivo)

    def __str__(self):
        return self.nome