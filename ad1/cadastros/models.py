from django.db import models

# Create your models here.
class Voluntario(models.Model):
    nome = models.CharField("nome do voluntário", max_length = 50)

    def __str__(self):
        return self.nome
    

