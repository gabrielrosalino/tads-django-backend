from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 

# Usuário voluntário
class Voluntario(models.Model): 
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='voluntario' 
    )
    nome = models.CharField(
        "Nome completo", 
        max_length=100
    )
    nascimento = models.DateField("Data de nascimento", null=True, blank=True)
    cpf = models.CharField(
        "CPF",
        max_length=14,
        # unique=True,
        null=False,
        blank=False
    )
    email = models.EmailField(
        "E-mail", 
        # unique=True
    )
    telefone_contato = models.CharField(
        "Telefone de Contato",
        max_length=20,
        blank=True
    )
    # Endereço
    rua = models.CharField("Rua", max_length=200)
    numero = models.CharField("Número", max_length=20)
    complemento = models.CharField("Complemento", max_length=100, blank=True)
    bairro = models.CharField("Bairro", max_length=100, blank=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True)
    estado = models.CharField("Estado", max_length=2, blank=True)
    cep = models.CharField("CEP", max_length=9, blank=True)
    descricao_atividades = models.TextField(
        "Descrição das Atividades/Interesses",
        blank=True
    )
    foto = models.ImageField(
        "Foto Principal",
        upload_to='voluntarios/perfis/fotos/',
        null=True,
        blank=True
    )

    # Status do voluntário
    STATUS_AGUARDANDO_DOCUMENTOS = 'AGUARDANDO_DOCUMENTOS'
    STATUS_ATIVO = 'ATIVO'
    STATUS_INATIVO = 'INATIVO'
    STATUS_PROCESSO_CHOICES = [
        (STATUS_AGUARDANDO_DOCUMENTOS, 'Aguardando Documentos'),
        (STATUS_ATIVO, 'Ativo'),
        (STATUS_INATIVO, 'Inativo'),
    ]
    status_processo_voluntario = models.CharField(
        "Status do Processo",
        max_length=50,  
        choices=STATUS_PROCESSO_CHOICES,
        default=STATUS_AGUARDANDO_DOCUMENTOS, 
        null=False,  
        blank=False 
    )

    #Tipo de voluntário
    TIPO_APOIO_ADMINISTRATIVO = 'APOIO_ADMINISTRATIVO'
    TIPO_PROFESSOR = 'PROFESSOR'
    TIPO_MONITOR = 'MONITOR'
    TIPO_OUTRO = 'OUTRO' 
    TIPO_VOLUNTARIO_CHOICES = [
        (TIPO_APOIO_ADMINISTRATIVO, 'Apoio Administrativo'),
        (TIPO_PROFESSOR, 'Professor(a)'),
        (TIPO_MONITOR, 'Monitor(a)'),
        (TIPO_OUTRO, 'Outro / Não especificado'), 
    ]
    tipo_voluntario = models.CharField(
        "Tipo de Voluntário",
        max_length=50,  
        choices=TIPO_VOLUNTARIO_CHOICES,
        default=TIPO_OUTRO, 
        null=False,
        blank=False 
    )
    # TODO Criar uma foreignKey que puxe as disciplinas listadas, caso o tipo_voluntario seja TIPO_PROFESSOR.

    data_inicio_processo = models.DateTimeField(
        "Data de Início do Processo",
        default=timezone.now, 
        null=False,            
        blank=True,           
        editable=False        
    )

    def __str__(self):
        return self.user.username 
    
# Modelo estudante.
class Aluno(models.Model):
    PERIODO_INTERESSE = (
        (0, "Matutino"),
        (1, "Vespertino"),
        (2, "Noturno"),
    )

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
    curso_interesse = models.ForeignKey(
        'Curso',
        verbose_name="Curso de Interesse",
        on_delete=models.SET_NULL,  # ou PROTECT, dependendo de como queira tratar exclusão
        null=True,                  # permite que inicialmente não tenha valor
        blank=False                 # torne obrigatório no formulário (pode mudar para True, se quiser opcional)
    )

    periodo_interesse = models.IntegerField(
        "Período de Interesse",
        choices=PERIODO_INTERESSE,
        default=0,            # <— define MATUTINO como padrão
    )

    # TODO: id_curso = models.ForeignKey(Curso)

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
    

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nome = models.CharField("Nome do curso", max_length=30, unique=True)

    def __str__(self):
        return self.nome

# Modelo Periodo Letivo
class Periodo_Letivo(models.Model):
    STATUS = {
        0: "INATIVO",
        1: "ATIVO"
    }

    id_periodo_letivo = models.AutoField(primary_key=True)
    ano = models.IntegerField("Ano do Período Letivo")
    semestre = models.IntegerField("Semestre do Período Letivo")
    nome = models.CharField("Nome do Período Letivo", max_length=30)
    data_inicio = models.DateField("Data de Início do Período Letivo")
    data_fim = models.DateField("Data do Final do Período Letivo")
    status = models.IntegerField("Status", choices=STATUS)

    class Meta:
        verbose_name = "Período Letivo"
        verbose_name_plural = "Períodos Letivos"
    
    def __str__(self):
        return self.nome