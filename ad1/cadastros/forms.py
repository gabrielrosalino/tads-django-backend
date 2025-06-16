from django import forms
from .models import Aluno

# cadastros/forms.py
from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            # Dados Pessoais
            "nome", "email", "contato", "nascimento", "nacionalidade", "naturalidade", "estado_civil",
            # Dados Familiares
            "nome_pai", "escolaridade_pai", "nome_mae", "escolaridade_mae",
            # Sócio-econômicos
            "renda_familiar",
            # Dados Residenciais
            "rua", "numero", "complemento", "bairro", "cidade", "estado", "cep",
            # Dados Institucionais
            "status", "curso_interesse", "periodo_interesse",
        ]
