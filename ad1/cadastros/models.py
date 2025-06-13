from django.db import models

# Modelo voluntário.
class Voluntario(models.Model):
    nome = models.CharField("nome do voluntário", max_length = 50)

    def __str__(self):
        return self.nome
    
# Modelo estudante.
class Student(models.Model):
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